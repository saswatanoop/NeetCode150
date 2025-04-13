
from typing import List, Optional
from collections import deque
# 1. https://leetcode.com/problems/number-of-islands/description/
def numIslands(self, grid: List[List[str]]) -> int:
    # T:O(n*m) S:O(n*m) modified the same grid to mark it as visited, but dfs stack is there
    def dfs(i,j):
        grid[i][j]="X"
        for d in directions:
            x,y=i+d[0],j+d[1]
            if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1":
                dfs(x,y)

    islands=0
    directions=[[0,1],[0,-1],[-1,0],[1,0]]
    n,m=len(grid),len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1":
                islands+=1
                dfs(i,j)
    # change back all visited 1s from X to 1
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="X":
                grid[i][j]=="1"
    return islands

# 2. https://leetcode.com/problems/max-area-of-island/
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # T:O(n*m) S:O(n*m) modified the same grid to mark it as visited, but dfs stack is there
    def dfs(i,j):
        grid[i][j]=2
        area=1
        for d in directions:
            x,y=i+d[0],j+d[1]
            if x>=0 and x<n and y>=0 and y<m and grid[x][y]==1:
                area+=dfs(x,y)
        return area

    maxArea=0
    directions=[[0,1],[0,-1],[-1,0],[1,0]]
    n,m=len(grid),len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                maxArea=max(maxArea,dfs(i,j))
    
    # change back all visited 1s from X to 1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                grid[i][j]==1
    return maxArea


# 3. https://leetcode.com/problems/clone-graph/
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    # T: O(V+E) S:O(V) for hash map, node is hashable as key as python uses address for custom objects as key
    if not node:
        return None
    cloned={}
    q=deque([node])
    cloned[node]=Node(node.val)

    while q:
        front=q.popleft()
        for nbr in front.neighbors:
            # add nbr vertex if not cloned 
            if nbr not in cloned:
                q.append(nbr)
                cloned[nbr]=Node(nbr.val)
            # add all the edges of front node to the cloned graph
            cloned[front].neighbors.append(cloned[nbr])
    return cloned[node]

# 4. https://neetcode.io/problems/islands-and-treasure
def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    # T:O(n*m) S:O(n*m) modified the same grid to mark it as visited, but dfs stack is there
    # Multi source BFS
    q=deque()
    rows,cols=len(grid),len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==0:
                q.append((i,j))
    while q:
        i,j=q.popleft()
        dist=grid[i][j]+1
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            x,y=i+d[0],j+d[1]
            if x>=0 and x<rows and y>=0 and y<cols and grid[x][y]>dist:
                grid[x][y]=dist
                q.append((x,y))

# 5. https://leetcode.com/problems/rotting-oranges/description/
def orangesRotting(self, grid: List[List[int]]) -> int:
    # T:O(n*m) S:O(n*m) q is used for BFS
    # Multi source layered BFS
    rows,cols=len(grid),len(grid[0])
    fresh=time=0
    q=deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==2:
                q.append((i,j))
            elif grid[i][j]==1:
                fresh+=1
    
    while q and fresh:
        time+=1
        size=len(q)
        for i in range(size):
            i,j=q.popleft()
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                x,y=i+d[0],j+d[1]
                if x>=0 and x<rows and y>=0 and y<cols and grid[x][y]==1:
                    grid[x][y]=2 #mistake: missed to convert fresh to rotten
                    q.append((x,y))
                    fresh-=1
    
    return -1 if fresh else time

# 7. https://leetcode.com/problems/surrounded-regions/
def solve(self, board: List[List[str]]) -> None:
    # T:O(n*m) S:O(n*m) modified the same grid to mark it as visited, but dfs stack is there
    def dfs(i,j):
        board[i][j]="S"
        for d in directions:
            x,y=i+d[0],j+d[1]
            if x>=0 and x<rows and y>=0 and y<cols and board[x][y]=="O":
                dfs(x,y)

    directions=[[0,1],[1,0],[-1,0],[0,-1]]
    rows,cols=len(board),len(board[0])

    # do Travesal from border O values
    for i in range(rows):
        for j in range(cols):
            if (i==0 or j==0 or i==rows-1 or j==cols-1) and board[i][j]=="O":
                dfs(i,j)
    
    #** we once check for value O at i,j so once we set it to O in elif conditon it won't be changed back
    for i in range(rows):
        for j in range(cols):
            if board[i][j]=="O":
                board[i][j]="X"
            elif board[i][j]=="S":
                board[i][j]="O"


# 10. https://neetcode.io/problems/valid-tree
from additional_data_structures import DSU
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    '''
        1. Connected: A graph with no cycles but not connected is called a forest, not a tree.
            connected componenets should be 1
        2. No cycles: A graph that is connected but has a cycle is not a tree.
    '''
    # T:O(V+E) S:O(V)
    dsu=DSU(n)
    for u,v in edges:
        if dsu.find_parent(u)!=dsu.find_parent(v):
            dsu.union(u,v)
        # There is a cycle, so not a Tree
        else:
            return False
    # Check if all nodes are connected
    return dsu.component_count==1


# 11. https://neetcode.io/problems/count-connected-components
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # T:O(V+E) S:O(V)
    dsu=DSU(n)
    for u,v in edges:
        if dsu.find_parent(u)!= dsu.find_parent(v):
            dsu.union(u,v)
    return dsu.component_count

# 12. https://leetcode.com/problems/redundant-connection/
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # T:O(V+E) S:O(V)
    dsu=DSU()
    for u,v in edges:
        if dsu.find_parent(u)==dsu.find_parent(v):
            return [u,v]
        else:
            dsu.union(u,v)
# 
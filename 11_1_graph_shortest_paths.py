from collections import defaultdict, deque
import heapq
from math import inf
from typing import List, Union

'''
1. BFS 
2. Dijkstra’s 
3. Toposort + Relax
4. 0 1 BFS
5. Bellman Ford
6. Floyd-Warshall
7. A*  
'''
# 1. Unit weight: Single source shortest path in Undirected/Directed Graph(Will work for both)
# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
def shortestPathBFS(adj, src):
    # T: O(V + E)
    # S: O(V)
    dist = [-1] * len(adj)
    dist[src] = 0
    q = deque([src])
    
    while q:
        node = q.popleft()
        for nbr in adj[node]:
            # if nbr not seen, we found the shortest distance for nbr
            if dist[nbr] == -1:
                q.append(nbr)
                dist[nbr] = dist[node] + 1

    return dist

# 2. Non-negative weights: Single source shortest path in Directed/Undirected With/Without cycles Graph using Dijkstra's Algorithm
# Dijkstra’s algorithm only works when all edge weights are non-negative
# https://leetcode.com/problems/network-delay-time/
def networkDelayTime(self, times: List[List[int]], n: int, k: int) :
    # T: O(E log V)
    # S: O(V + E)
    # Build Adjacency list of graph
    graph=defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))
    
    # Dijkstra's algorithm
    dist=[inf]*(n+1)
    min_heap=[(0,k)]
    dist[k]=0
    seen=0

    while min_heap:
        d,node=heapq.heappop(min_heap)
        # lower distance already computed, ignore current
        # don't use d>=dist[node] as at start dist[k] is 0 and we push (0,k) to heap
        if d>dist[node]: 
            continue
        # Exit early if all nodes distance have been computed, but pq is not empty yet
        seen+=1
        if seen==n:
            break

        for nbr,w in graph[node]:
            dist_using_node=d+w
            if dist[nbr]>dist_using_node:
                # Sets the distance for nbr, and with this only values lower than current distance for nbr can be pushed to pq
                dist[nbr]=dist_using_node
                heapq.heappush(min_heap,(dist_using_node,nbr))
    
    # Use generator to compute max value, dont use dist[1:] it will create a copy and take extra space
    ans = max(dist[i] for i in range(1, n + 1))
    return -1 if ans==inf else ans

# 3. Any(pos/neg) Weight: DAG Single source shortest path
# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
def shortestPath(V: int, E: int, edges: List[List[int]]) -> List[Union[int, float]]:
    # T: O(V + E), S: O(V + E)
    def dfs(node):
        visited[node] = True
        for nbr, w in adj[node]:
            if not visited[nbr]:
                dfs(nbr)
        topo.append(node)

    # build adjacency list
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))

    # generate topological order
    visited = [False] * V
    topo = []
    for i in range(V):
        if not visited[i]:
            dfs(i)
    topo.reverse()

    
    dist = [inf] * V
    dist[0] = 0  # assuming 0-based source

    # compute shortest distance using topo order
    for node in topo:
        # all nodes before src will have inf distance
        if dist[node] == inf:
            continue
        for nbr, w in adj[node]:
            if dist[nbr] > dist[node] + w:
                dist[nbr] = dist[node] + w
    
    # convert inf to -1 as per problem statement
    for i in range(V):
        if dist[i] == inf:
            dist[i] = -1
    
    return dist
            
# 4. 0-1 weights: single source shortest path in Directed/Undirected Graph
# 0-1 BFS is an optimization over Dijkstra's algorithm for graphs where edge weights are either 0 or 1.
def zero_one_bfs(n, graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    dq = deque([src])

    while dq:
        u = dq.popleft()
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                # push to left as it did not increase distance, else to right
                if w == 0:
                    dq.appendleft(v)
                # Lemma : During the execution of BFS, the queue holding the vertices only contains elements from at max two successive levels of the BFS tree
                # Thus if we add a node with weight 1 it will be at most one level deeper than current node, all other one level deeper nodes are already in dq with max distance of dist[u]+1
                else:
                    dq.append(v)
    return dist
        
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
class Solution:
    def minimumObstacles(self, grid: List[List[int]]):
        n,m=len(grid),len(grid[0])
        dist=[[inf]*m for _ in range(n)]
        dist[0][0]=0
        q=deque([(0,0)])

        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            row,col=q.popleft()
            if row==n-1 and col==m-1:
                break
            for dx,dy in direction:
                x,y=row+dx,col+dy
                if 0<=x<n and 0<=y<m:
                    weight=grid[x][y]
                    if dist[x][y]>dist[row][col]+weight:
                        dist[x][y]=dist[row][col]+weight
                        if weight==0:
                            q.appendleft((x,y))
                        else:
                            q.append((x,y))

        return dist[n-1][m-1]

# 5. Any(pos/neg) Weights: Single source shortest path in Directed/Undirected Graph using Bellman-Ford Algorithm
# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0
def bellmanFord(self, V, edges, src):
    # T: O(V * E), S: O(V)
    INF = int(1e8)
    dist=[INF]*V
    dist[src]=0
    
    for i in range(V):
        updated = False
        for u,v,w in edges:
            if dist[u]==INF:
                continue
            if dist[u]+w<dist[v]:
                # below if checks for negative cycles
                if i==V-1:
                    return [-1]
                dist[v]=dist[u]+w
                updated = True
        
        if not updated:          # <---- no edge was relaxed in this pass
            break                # <---- stop early
                
    return dist

# 6. Any(pos/neg) weights: All pairs shortest path in Directed/Undirected Graph using Floyd-Warshall Algorithm
# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
def floydWarshall(self, dist):
    # T: O(V^3), S: O(V^2)
    INF=int(1e8)
    vertexes=len(dist)
    
    for k in range(vertexes):
        for i in range(vertexes):
            if dist[i][k]!=INF:
                for j in range(vertexes):
                    if dist[k][j]!=INF:
                        new_distance=dist[i][k]+dist[k][j]
                        if dist[i][j]>new_distance:
                            dist[i][j]=new_distance
    
    for i in range(vertexes):
        if dist[i][i]<0: #negative weight cycles
            return [-1]
    return dist
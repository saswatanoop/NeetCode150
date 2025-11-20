


'''
MST:
1. Kruskal's Algorithm: DSU + greedy T:O(ElogE) S:O(V)
2. Prim's Algorithm: Greedy + min-heap T:O(ElogV) S:O(V) as E=V^2 in dense graph, O(ElogE) = O(ElogV^2) = O(2ElogV) = O(ElogV)


Tarjan’s Algorithm:
1. Articulation Points
2. Bridges
3. Strongly Connected Components (SCC)

'''

from additional_data_structures import DSU
from collections import defaultdict
import heapq

class MST:
    def spanningTree_Kruskal(self, V, edges):
        # 1. Kruskal's Algorithm: DSU + greedy T:O(ElogE) S:O(V)
        edges.sort(key=lambda x: x[2])
        dsu=DSU(V)
        edges_count=0
        mst_sum=0
        
        for u,v,w in edges:
            if dsu.find_parent(u)!=dsu.find_parent(v):
                dsu.union(u,v)
                edges_count+=1
                mst_sum+=w
                # Early stopping
                if edges_count==V-1:
                    break
        
        # Very Important check for disconnected graph
        if edges_count != V - 1:
            return -1  # Graph is disconnected, MST not possible
        
        return mst_sum

    def spanningTree_Prims(self, V, edges):
        # 2. Prim's Algorithm: Greedy + min-heap T:O(ElogV) S:O(V) as E=V^2 = O(ElogV)
        adjList=defaultdict(list)
        for u,v,w in edges:
            adjList[u].append((v,w))
            adjList[v].append((u,w))
            
        mst_sum=0
        min_heap=[(0,0,-1)] #weight, node, parent
        visited=set()
        
        while min_heap:
            weight,node,parent=heapq.heappop(min_heap)
            
            # Mark the visited only while poping from heap
            if node not in visited:
                visited.add(node)
                mst_sum+=weight
                # edge will be parent->node
                
                for nbr,w in adjList[node]:
                    if nbr not in visited:
                        heapq.heappush(min_heap,(w,nbr,node))
            # Early stopping
            if len(visited)==V:
                break

        # Very Important check for disconnected graph
        if len(visited)!=V:
            return -1  # Graph is disconnected, MST not possible
        
        return mst_sum

# 2. Tarjan’s Algorithm:
 
# Articulation Points and Bridges in an undirected graph: https://leetcode.com/problems/critical-connections-in-a-network/                
def find_ap_and_bridges(n, edges):
    def dfs_helper(node, parent):
        nonlocal timer
        disc[node] = low[node] = timer
        timer += 1

        children = 0 # for root Articulation Point check

        for nbr in adj[node]:
            # unvisited child
            if disc[nbr] == -1:               
                children += 1
                dfs_helper(nbr, node)

                # use nbr's low value to update node's low value
                low[node] = min(low[node], low[nbr])

                # for node->nbr check articulation point and bridge
                # bridge condition
                if low[nbr] > disc[node]:
                    bridges.append((node, nbr))

                # Check articulation point for non-root nodes
                if parent != -1 and low[nbr] >= disc[node]:
                    articulation_points.add(node)

            # back edge
            elif nbr != parent:
                # update low value for back edge
                low[node] = min(low[node], disc[nbr])

        # check if root is an articulation point
        if parent == -1 and children > 1:
            articulation_points.add(node)

    from collections import defaultdict
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n        # -1 means unvisited
    low  = [-1] * n
    timer = 0

    articulation_points = set()
    bridges = []

    for i in range(n):
        if disc[i] == -1:
            dfs_helper(i, -1)

    return articulation_points, bridges

# Strongly Connected Components (SCC) in Directed Graph using Tarjan's Algorithm
from collections import defaultdict

def find_sccs_tarjan(n, edges):
    def dfs_helper(node):
        nonlocal timer
        disc[node] = low[node] = timer
        timer += 1
        
        # Add to stack and mark as present
        stack.append(node)
        on_stack[node] = True
        
        for nbr in adj[node]:
            if disc[nbr] == -1:
                dfs_helper(nbr)
                # use nbr's low value to update node's low value
                low[node] = min(low[node], low[nbr])
                
            # Back Edge: nbr is visited AND is currently in the recursion stack: This determines the cycle
            elif on_stack[nbr]:
                # update low value for back edge
                low[node] = min(low[node], disc[nbr])
            
            # NOTE: If nbr was visited but NOT on_stack, it's a Cross Edge to a completed SCC. We simply ignore it.

        # Check if 'node' is the root of an SCC
        if low[node] == disc[node]:
            current_scc = []
            while True:
                top = stack.pop()
                on_stack[top] = False
                current_scc.append(top)
                # Stop once we pop the root (node)
                if top == node:
                    break
            all_sccs.append(current_scc)

    # Graph Setup (Directed)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v) 

    disc = [-1] * n
    low = [-1] * n
    timer = 0
    
    # Stack for tracking nodes in the current path
    stack = []
    on_stack = [False] * n # O(1) lookup to check if node is in stack
    
    all_sccs = []

    for i in range(n):
        if disc[i] == -1:
            dfs_helper(i)
            
    return all_sccs
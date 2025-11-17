


'''
MST:
1. Kruskal's Algorithm: DSU + greedy T:O(ElogE) S:O(V)
2. Prim's Algorithm: Greedy + min-heap T:O(ElogV) S:O(V) as E=V^2 in dense graph, O(ElogE) = O(ElogV^2) = O(2ElogV) = O(ElogV)

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
                    
                

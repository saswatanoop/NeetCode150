


'''
MST:
1. Krushal's Algorithm: DSU + greedy T:O(ElogE) S:O(V)
2. Prim's Algorithm: Greedy + min-heap T:O(ElogV) S:O(V)

'''

from additional_data_structures import DSU

def spanningTree(V, edges):
    edges.sort(key=lambda x: x[2])
    dsu=DSU(V)
    edges_count=0
    mst_sum=0
    
    for u,v,w in edges:
        if dsu.find_parent(u)!=dsu.find_parent(v):
            dsu.union(u,v)
            edges_count+=1
            mst_sum+=w
            if edges_count==V-1:
                break
    
    # Very Important check for disconnected graph
    if edges_count != V - 1:
        return -1  # Graph is disconnected, MST not possible
    
    return mst_sum
                
                


from typing import List
from collections import defaultdict
import heapq


# 1. https://leetcode.com/problems/network-delay-time/
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # T:O(ElogE)=>ElogV^2=>2ELogV S:O(V+E)
    # Dijkstra's algorithm
    graph=defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))

    dist=[float("inf")]*(n+1)
    min_heap=[]
    
    heapq.heappush(min_heap,(0,k))
    dist[k]=0
    dist[0]=0

    while min_heap:
        d,node=heapq.heappop(min_heap)
        for nbr,w in graph[node]:
            dist_using_node=d+w
            if dist[nbr]>dist_using_node:
                heapq.heappush(min_heap,(dist_using_node,nbr))
                dist[nbr]=dist_using_node
    # print(dist)
    max_dist=max(dist)
    return -1 if max_dist==float("inf") else max_dist

# 3. https://leetcode.com/problems/min-cost-to-connect-all-points/description/
from additional_data_structures import DSU
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # T:O(n^2logn) S:O(n) n^2log(n^2)=>2(n^2)logn 
    # Kruskal's algorithm: for finding MST
    
    edges=[]
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            weight= abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
            edges.append((weight,i,j))
    # Sort edges based on weight, T:O(ElogE) E=n^2
    edges.sort()
    dsu=DSU(len(points))
    cost=0

    # Iterate through edges and add to MST, T:O(E)
    for w,u,v in edges:
        if dsu.component_count ==1:
            break    
        if dsu.find_parent(u)!=dsu.find_parent(v):
            cost+=w
            dsu.union(u,v)
    return cost

# 
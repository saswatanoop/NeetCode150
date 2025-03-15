
from typing import List 
from collections import defaultdict, OrderedDict
import heapq

# 1. https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap=[]
        self.size=k
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        # T:O(logk) and S:O(k)
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.size:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# 2. https://leetcode.com/problems/last-stone-weight/
def lastStoneWeight(stones: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    max_heap=[]
    for s in stones:
        heapq.heappush(max_heap,(-s,s))

    while len(max_heap)>1:
        top1=heapq.heappop(max_heap)[1]
        top2=heapq.heappop(max_heap)[1]
        weight=top1-top2
        if weight>0:
            heapq.heappush(max_heap,(-weight,weight))

    return max_heap[0][1] if max_heap else 0

# 3. https://leetcode.com/problems/k-closest-points-to-origin/
def kClosest( points: List[List[int]], k: int) -> List[List[int]]:
    # T:O(nlogk) and S:O(k)
    max_heap = []
    for point in points:
        distance = point[0]*point[0]+point[1]*point[1]
        heapq.heappush(max_heap,(-distance,point))
        if len(max_heap)>k:
            heapq.heappop(max_heap)
    return [point[1] for point in max_heap]

# 4. https://leetcode.com/problems/kth-largest-element-in-an-array/
def findKthLargest(self, nums: List[int], k: int) -> int:
    # T:O(nlogk) and S:O(k)
    min_heap=[]
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    return min_heap[0]
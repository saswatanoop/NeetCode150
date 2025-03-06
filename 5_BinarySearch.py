from typing import List
from collections import defaultdict

# 1. https://leetcode.com/problems/binary-search/
def search( nums: List[int], target: int) -> int:
    # T:O(logn) and S:O(1)
    s,e=0,len(nums)-1
    
    while s<=e:
        mid=s+(e-s)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            s=mid+1
        else:
            e=mid-1
            
    return -1

# 2. https://leetcode.com/problems/search-a-2d-matrix/description/
import bisect
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # T:O(logn + logm) and S:O(1)
    # compare with smallest and largest element in matrix first
    if target<matrix[0][0] or target>matrix[-1][-1]:
        return False
    
    s,e=0,len(matrix)-1
    while s<e:
        mid =s+(e-s)//2
        if matrix[mid][-1]<target:
            s=mid+1
        # it might be in mid row so we can't set e=mid-1
        else:
            e=mid
    # when s==e, we need to search in that row for the element
    pos = bisect.bisect_left(matrix[s], target)
    return pos<len(matrix[s]) and matrix[s][pos]==target 

# 3. https://leetcode.com/problems/koko-eating-bananas/
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # T: O(n*log(max_pile_value)) S:O(1)
    def possible_to_eat():
        speed=mid
        time_needed=0
        for p in piles:
            time_needed+=p//speed
            if p%speed!=0:
                time_needed+=1
        return time_needed<=h

    # ans space in between min_speed and max_speed, use binary search
    min_speed=1
    max_speed=max(piles)
    ans=max_speed

    while min_speed<=max_speed:
        mid=min_speed+(max_speed-min_speed)//2
        if possible_to_eat():
            ans=mid
            max_speed=mid-1
        else:
            min_speed=mid+1
    return ans

# 6. https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.dict=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # T:O(1) and S:O(n*m) where n is number of keys and m is number of values
        self.dict[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        # T:O(logm) and S:O(1) where m is number of values for the key
        if key not in self.dict or timestamp<self.dict[key][0][0]:
            return ""
        ans=None
        s,e=0,len(self.dict[key])-1
        while s<=e:
            mid=s+(e-s)//2
            if  self.dict[key][mid][0]<=timestamp:
                ans=self.dict[key][mid][1]
                s=mid+1
            else:
                e=mid-1
        return ans
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
    def possible_to_eat(speed):
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
        if possible_to_eat(mid):
            ans=mid
            max_speed=mid-1
        else:
            min_speed=mid+1
    return ans

# 4. https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
def findMin(self, nums: List[int]) -> int:
    # T: O(logn) S:O(1)
    s,e=0,len(nums)-1

    while s<=e:
        if nums[s]>nums[e]: # there is rotation present between [s,e]
            mid=s+(e-s)//2
            if nums[mid]>=nums[s]: #we are in 1st rotated section
                s=mid+1
            else:# nums[mid]<nums[s] we are in 2nd rotated section
                e=mid
        else: # there is no rotation remaining and [s,e] is sorted
            return nums[s]
            
        
# 5. https://leetcode.com/problems/search-in-rotated-sorted-array/
def search(self, nums: List[int], target: int) -> int:
    # T:O(logn) and S:O(1)
    # 1,2 and 3rd will work as normal binary search when [s,e] is sorted
    # use the knowledge, if mid falls in 1st half, [s,mid] is sorted, if mid falls in 2nd half, [mid,e] is sorted
    s,e=0,len(nums)-1
    while s<=e:
        mid=s+(e-s)//2
        if nums[mid]==target: #1
            return mid
        elif nums[s]<=target<nums[mid]: #2
            e=mid-1
        elif nums[mid]<target<=nums[e]: #3
            s=mid+1
        # Mistake: nums[s]<nums[mid], even if it is equal we know it is not there in s
        elif nums[s]<=nums[mid]: #4 the target is definitely not b/w [s,mid] , confirmed in 2nd
            s=mid+1
        else: #5 
            e=mid-1
    return -1 

        
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
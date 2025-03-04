from typing import List

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
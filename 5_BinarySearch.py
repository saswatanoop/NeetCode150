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

# 2. https://leetcode.com/problems/search-a-2d-matrix/description/
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

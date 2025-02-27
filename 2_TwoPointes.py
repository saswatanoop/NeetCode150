from typing import List


# 1. https://leetcode.com/problems/valid-palindrome/description/
def isPalindrome(self, s: str) -> bool:
    # T:O(n) S:O(1)
    i,j=0,len(s)-1
    while i<j:
        while i<j and not s[i].isalnum():
            i+=1
        while i<j and not s[j].isalnum():
            j-=1
        if i<j and s[i].lower()!=s[j].lower():
            return False
        i+=1
        j-=1
    return True

# 2. https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # T:O(n) and S:O(1)
    i,j=0,len(nums)-1

    while i<j:
        total= nums[i]+nums[j]
        if total==target:
            return [i+1,j+1]
        elif total>target:
            j-=1
        else:
            i+=1

# 3.

# 4. https://leetcode.com/problems/container-with-most-water/
def maxArea(self, height: List[int]) -> int:
    # T:O(n) and S:O(1)
    s,e=0,len(height)-1
    water=0

    while s<e:
        h=min(height[s],height[e])
        water=max(water,h*(e-s))
        if height[s]>height[e]:
            e-=1
        else:
            s+=1
        
    return water

# 5. https://leetcode.com/problems/trapping-rain-water/
def trap(self, height: List[int]) -> int:
    # T:O(n) and S:O(1)
    max_l=max_r=0
    trapped_water=0
    s,e=0,len(height)-1

    while s<=e:
        if max_l<max_r:
            trapped_water+=max(0,max_l-height[s])
            max_l=max(max_l,height[s])
            s+=1
        else:
            trapped_water+=max(0,max_r-height[e])
            max_r=max(max_r,height[e])
            e-=1
    return trapped_water
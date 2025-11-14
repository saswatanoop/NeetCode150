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
def twoSum(self, nums: List[int], target: int):
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

# 3. https://leetcode.com/problems/3sum/description/
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # T:O(n^2) and S:O(1) if modifying input is allowed and sorting takes O(1) space
    nums.sort()
    triplets=[]

    i=0
    while i<len(nums):
        two_sum=0-nums[i]
        s=i+1
        e=len(nums)-1
        while s<e:
            cur_sum=nums[s]+nums[e]
            if cur_sum>two_sum:
                e-=1
            elif cur_sum<two_sum:
                s+=1
            else:
                triplets.append([nums[i],nums[s],nums[e]])
                s+=1
                # Don't use same value as nums[s] again as first number of pair
                while s<e and nums[s]==nums[s-1]:
                    s+=1
        # Don't use same value as nums[i] again as first number of triplet
        i+=1
        while i<len(nums) and nums[i]==nums[i-1]:
            i+=1
    return triplets

# 4. https://leetcode.com/problems/container-with-most-water/
def maxArea(self, height: List[int]) -> int:
    # T:O(n) and S:O(1)
    s,e=0,len(height)-1
    max_water=0

    while s<e:
        allowed_height=min(height[s],height[e])
        cur_water_capacity=allowed_height*(e-s)
        max_water=max(max_water,cur_water_capacity)
        # keep the higher height as it can be useful later
        if height[s]>height[e]:
            e-=1
        else:
            s+=1
        
    return max_water

# 5. https://leetcode.com/problems/trapping-rain-water/
def trap(self, height: List[int]) -> int:
    # T:O(n) and S:O(1)
    total_water=0
    maxh_left=maxh_right=0 #max height on both sides
    
    # compute water collected at one of the ends and keep moving inwards
    s,e=0,len(height)-1
    while s<=e:
        if maxh_left<maxh_right:
            water=max(0,maxh_left-height[s])
            maxh_left=max(maxh_left,height[s])
            s+=1
        else:
            water=max(0,maxh_right-height[e])
            maxh_right=max(maxh_right,height[e])
            e-=1
        total_water+=water
    
    return total_water

# 
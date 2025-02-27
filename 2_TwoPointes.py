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

# 3. https://leetcode.com/problems/3sum/description/
def threeSum(self, nums_orig: List[int]) -> List[List[int]]:
    # T:O(n^2) and S:O(1) if modifying input is allowed and sorting takes O(1) space
    def two_sum(start,target):
        two_sums=[]
        # Mistake: used s=0 
        s,e=start,n-1

        while s<e:
            cur=nums[s]+nums[e]
            if cur==target:
                two_sums.append([nums[s],nums[e]])
                e-=1
                s+=1
                while s<e and nums[s]==nums[s-1]:
                    s+=1
            elif cur>target:
                e-=1
            else:
                s+=1
        return two_sums
    
    nums=sorted(nums_orig)
    three_sums=[]
    i=0
    n=len(nums)
    # Three sum logic
    while i<n:
        all_pairs=two_sum(i+1,0-nums[i])
        for p in all_pairs:
            three_sums.append([nums[i],p[0],p[1]])
        i+=1
        while i<n and nums[i]==nums[i-1]:
            i+=1
    
    return three_sums

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
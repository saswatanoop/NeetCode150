
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

# 4.

# 5.
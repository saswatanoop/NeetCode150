from typing import List


# 1. https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray( nums: List[int]) -> int:
    # Kadane's algorithm: T:O(n) S:O(1)
    
    # State: lsum = max sum of subarray ending at i
    # At each i: lsum = max(lsum + nums[i], nums[i]) - extend or start fresh
    lsum = gsum = nums[0]
    n = len(nums)
    for i in range(1, n):
        lsum = max(lsum + nums[i], nums[i])
        gsum = max(gsum, lsum)
    return gsum

# 2. https://leetcode.com/problems/jump-game/
def canJump(self, nums: List[int]) -> bool:
    # T:O(n) and S:O(1)
    # Track a growing reachable interval [0, farthest]; every reachable position can extend the interval further.
    i=0
    max_reach=0
    n=len(nums)
    while i<=max_reach:
        max_reach=max(max_reach,i+nums[i])
        if max_reach>=n-1:
            return True
        i+=1
    return False
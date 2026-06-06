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
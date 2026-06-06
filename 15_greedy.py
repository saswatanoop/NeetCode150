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
    # Greedy Reachability: Maintain the farthest reachable position.
    i=0
    max_reach=0
    n=len(nums)
    while i<=max_reach:
        max_reach=max(max_reach,i+nums[i])
        if max_reach>=n-1:
            return True
        i+=1
    return False

# 3. https://leetcode.com/problems/jump-game-ii/description/
def jump(self, nums: List[int]) -> int:
    # T:O(n) and S:O(1)
    # Greedy Level Expansion: Treat the current reachable range as one jump; expand it to the farthest next range and count expansions.
    l=r=0
    max_reach=0
    n=len(nums)
    jumps=0

    while max_reach<n-1: #once n-1 is reached we achieved the goal
        for i in range(l,r+1):
            max_reach=max(max_reach,i+nums[i])
        jumps+=1
        l=r+1
        r=max_reach
    return jumps
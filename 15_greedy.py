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

# 4: https://leetcode.com/problems/gas-station/description/
# T:O(n) and S:O(1)
def canCompleteCircuit(self, gas_available: List[int], gas_consumption: List[int]) -> int:
    n = len(gas_available)

    # If total consumption exceeds total available, no solution exists
    if sum(gas_available) - sum(gas_consumption) < 0:
        return -1

    res = 0
    cur_gas = 0
    for i in range(n):
        cur_gas += gas_available[i] - gas_consumption[i]

        if cur_gas < 0:
            # Proof that no station in (res, i] can be a valid start:
            # Assume some m in (res, i] is valid, then it must survive to i:
            #   sum(diff[k] for k in [m, i]) >= 0  ...(1)
            #
            # But we started at res and survived until m-1, so:
            #   sum(diff[k] for k in [res, m-1]) >= 0  ...(2)
            #
            # Adding (1) and (2):
            #   sum(diff[k] for k in [res, i]) >= 0
            #
            # Contradiction — cur_gas < 0 means this sum is negative.
            # So no m in (res, i] is valid → next candidate is i + 1.
            cur_gas = 0
            res = i + 1

    return res

# 5. https://leetcode.com/problems/hand-of-straights/description/
from collections import Counter
from sortedcontainers import SortedDict # type: ignore

def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    # T:O(nlogn) and S:O(n)
    # Pattern: Greedy Frequency Counting with Sorted Access, 
    # pick the smallest card and try to form a group of size groupSize with consecutive cards, if not possible return False. 
    n=len(hand)
    if n%groupSize != 0:
        return False
    
    no_of_groups = n//groupSize
    freq = Counter(hand)
    sorted_dic = SortedDict(freq.items())

    for _ in range(no_of_groups):
        key,value=sorted_dic.peekitem(0) # smallest card must start a group
        for _ in range(groupSize):
            if key not in sorted_dic:
                return False
            sorted_dic[key]-=1
            if sorted_dic[key]==0:
                sorted_dic.pop(key)
            key+=1 # There should be groupSize continous items, starting with smallest

    return True
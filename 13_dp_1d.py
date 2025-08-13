from typing import List
from collections import defaultdict, Counter
import heapq


# 1. https://leetcode.com/problems/climbing-stairs/
def climbStairs(n: int) -> int:
    # T:O(n) and S:O(n) for memoization
    # Base cases added in dictionary
    memo = {0: 1, 1: 1}

    def ways_to_reach(n):
        if n in memo:
            return memo[n]
        memo[n] = ways_to_reach(n - 1) + ways_to_reach(n - 2)
        return memo[n]

    return ways_to_reach(n)


# 2. https://leetcode.com/problems/min-cost-climbing-stairs/
def minCostClimbingStairs(self, cost: List[int]) -> int:
    # T:O(n) and S:O(n) for memoization
    n = len(cost)
    memo = {0: 0, 1: 0}

    # compute the cost taken to reach the index
    def reaching_cost(index):
        # already computed
        if index in memo:
            return memo[index]

        # reach i-1 and i-2 and add jump cost from there
        memo[index] = min(
            reaching_cost(index - 1) + cost[index - 1],
            reaching_cost(index - 2) + cost[index - 2],
        )

        return memo[index]

    return reaching_cost(n)


# 3. https://leetcode.com/problems/house-robber/description/
def rob(nums: List[int]) -> int:
    # T:O(n) and S:O(n) for memoization
    n = len(nums)
    memo = {}

    def robbed_amount(n):
        # No house
        if n < 0:
            return 0
        # Only one house, then steal it
        if n == 0:
            return nums[0]
        if n in memo:
            return memo[n]
        memo[n] = max(robbed_amount(n - 1), robbed_amount(n - 2) + nums[n])
        return memo[n]

    return robbed_amount(n - 1)


# 4. https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        # There is only one house
        if len(nums) == 1:
            return nums[0]
        # try 0 to n-2 and 1 to n-1, as n-1 and 0 are not allowed together in circular arrangement
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def robbed_amount(n):
            # No house
            if n < 0:
                return 0
            # Only one house, then steal it
            if n == 0:
                return nums[0]
            if n in memo:
                return memo[n]
            memo[n] = max(robbed_amount(n - 1), robbed_amount(n - 2) + nums[n])
            return memo[n]

        return robbed_amount(n - 1)

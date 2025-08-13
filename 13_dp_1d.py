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

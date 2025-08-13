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


# 2.

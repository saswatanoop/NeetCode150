# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_pos=defaultdict(list)
        for i in range(len(nums)):
            num_pos[nums[i]].append(i)
        
        ans=float("inf")

        for values in num_pos.values():
            if len(values)>2:
                for i in range(1, len(values)-1):
                    dist=2*(values[i+1]-values[i-1])
                    ans=min(ans,dist)
        return ans if ans != float("inf") else -1 # type: ignore

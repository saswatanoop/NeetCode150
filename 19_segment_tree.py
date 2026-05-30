# https://leetcode.com/problems/range-sum-query-mutable/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        from DS_segment_tree import SegmentTree
        # T: O(n) to build the tree, S: O(n) for the tree array
        self.segment_tree=SegmentTree(nums)
        
    # T: O(logn) to update, S: O(1) for the update function
    def update(self, index: int, val: int) -> None:
        self.segment_tree.point_update(index,val)
        
    # T: O(logn) to query, S: O(1) for the query function
    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.query(left,right)
        


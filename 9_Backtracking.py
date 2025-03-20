from typing import  List
from collections import Counter

# 1. https://leetcode.com/problems/subsets/
def subsets(self, nums: List[int]) -> List[List[int]]:
    def find_subset(index):
        if index==len(nums):
            all_subsets.append(cur_set[:])
        else:
            # ignore current index
            find_subset(index+1)
            cur_set.append(nums[index])
            find_subset(index+1)
            cur_set.pop()
    
    all_subsets=[]
    cur_set=[]
    find_subset(0)
    return all_subsets

# 2. https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # T:O(2^n) and S:O(n)
        def find_subset(index):
            if index==len(freq_list):
                all_subsets.append(cur_subset[:])
            else:
                # ignore current index
                find_subset(index+1)
                # use current index
                if freq_list[index][1]>0:
                    freq_list[index][1]-=1
                    cur_subset.append(freq_list[index][0])
                    find_subset(index)
                    freq_list[index][1]+=1
                    cur_subset.pop()

        freq_list=Counter(nums)
        freq_list=[[k,v] for k,v in freq_list.items()]
        cur_subset=[]
        all_subsets=[]
        find_subset(0)
        return all_subsets
# 9. https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations( digits: str) -> List[str]:
    # T:O(4^n) and S:O(n)
    def find_combination(index):
        if index==len(digits):
            all_combs.append(''.join(cur_comb))
        else:
            for c in keypad[digits[index]]:
                cur_comb.append(c)
                find_combination(index+1)
                cur_comb.pop()
    
    if not digits:
        return []

    keypad={
        '2':"abc",'3':"def",'4':"ghi",'5':"jkl",
        '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"
    }
    all_combs=[]
    cur_comb=[]
    find_combination(0)
    return all_combs

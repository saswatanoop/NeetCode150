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

# 3. https://leetcode.com/problems/combination-sum/
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # T:O(2^(n)) and S:O(n)
    # choose number one by one if choosen remain at same index
    # if target==0 found one answer
    # if reached end of list no comb found for cur list
    def find_combination(target,index):
        if target==0:
            all_combs.append(cur_comb[:])
        elif index==len(candidates):
            return 
        else:
            # ignore current
            find_combination(target,index+1)
            # use current number
            if target >= candidates[index]:
                cur_comb.append(candidates[index])
                find_combination(target-candidates[index],index)
                cur_comb.pop()
    
    cur_comb=[]
    all_combs=[]
    find_combination(target,0)
    return all_combs

# 4. https://leetcode.com/problems/combination-sum-ii/
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # T:O(2^(n)) and S:O(n)
    def find_combination(target,index):
        if target==0:
            all_combs.append(cur_comb[:])
        elif index==len(freq_list):
            return
        else:
            # ignore current index
            find_combination(target,index+1)
            # use current index
            if target >= freq_list[index][0] and freq_list[index][1]>0:
                freq_list[index][1]-=1
                cur_comb.append(freq_list[index][0])
                find_combination(target- freq_list[index][0],index)
                freq_list[index][1]+=1
                cur_comb.pop()

    freq_list=Counter(candidates)
    freq_list=[[k,v] for k,v in freq_list.items()]
    cur_comb=[]
    all_combs=[]
    find_combination(target,0)
    return all_combs

# 7. https://leetcode.com/problems/word-search/description/
def exist(self, board: List[List[str]], word: str) -> bool:
    # check at each board pos i,j for word
    # if the letter matches mark the board[i][j] and move to next 4, when combing back unmark it
    # return True if found in anyone

    def find_word(i,j,index):
        if index==len(word):
            return True
        if i<0 or i>=rows or j<0 or j>=cols or board[i][j]=='#' or board[i][j]!=word[index]:
            return False
        # ther is a match
        board[i][j]="#"
        for d in directions:
            x,y=i+d[0],j+d[1]
            if find_word(x,y,index+1):
                board[i][j]=word[index] #restore before returning True as well
                return True
        # restore the board[i][j] value, using the word, we don't need to store the char of board[i][j]
        board[i][j]=word[index]
        return False

    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    rows,cols=len(board),len(board[0])
    for i in range(rows):
        for j in range(cols):
            if find_word(i,j,0):
                return True
    return False

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

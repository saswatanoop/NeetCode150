from typing import  List
from collections import Counter

# 1. https://leetcode.com/problems/subsets/
def subsets(self, nums: List[int]) -> List[List[int]]:
    # T:O(2^n) and S:O(n)
    def find_subset(index):
        if index==len(nums):
            all_subsets.append(cur_set[:])
        else:
            # ignore current index
            find_subset(index+1)
            # chooses the current index
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
            # ** use current index, if the number of items are still left and remain at same index
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
            # use current index, if eligible and remain at same index to choose again
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
            # use current index, if eligible according to freq and target value and then remain at same index to choose again
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

# 5. https://leetcode.com/problems/permutations/
def permute(self, nums: List[int]) -> List[List[int]]:
    # T:O(n*n!) and S:O(n) n! permutations and n for each perm to copy to all_perm        
    def find_perm_with_swap(index):
        if index==len(nums):
            all_perm.append(nums[:])
        else:
            for i in range(index,len(nums)):
                nums[index],nums[i]=nums[i],nums[index]
                find_perm_with_swap(index+1)
                nums[index],nums[i]=nums[i],nums[index]

    def find_perm_without_swap():
        if len(perm)==len(nums):
            all_perm.append(perm[:])
        else:
            for i in range(len(visited)):
                if not visited[i]:
                    visited[i]=True
                    perm.append(nums[i])
                    find_perm_without_swap()
                    perm.pop()
                    visited[i]=False
    
    all_perm=[]
    find_perm_with_swap(0)
    # below 3 are needed for without swap
    perm=[]
    visited=[False]*len(nums)
    # find_perm_without_swap()
    return all_perm

# 6. https://leetcode.com/problems/permutations-ii/
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # T:O(n*n!) and S:O(n) n! permutations and n for each perm to copy to all_perm
    def find_perm_with_swap(index):
        if index==len(nums):
            all_perm.append(nums[:])
        else:
            seen=set() # to avoid duplicates, once a number is swapped with index, dont do it again
            for i in range(index,len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[index],nums[i]=nums[i],nums[index]
                    find_perm_with_swap(index+1)
                    nums[index],nums[i]=nums[i],nums[index]

    def find_perm():
        if len(perm)==len(nums):
            all_perm.append(perm[:])
        else:
            #  in perm list, we have to make sure at each index we are not repeating the same number, so we choose from freq list
            for i in range(len(freq)):
                if freq[i][1]>0:
                    freq[i][1]-=1
                    perm.append(freq[i][0])
                    find_perm()
                    perm.pop()
                    freq[i][1]+=1

    all_perm=[]
    find_perm_with_swap(0)
    # below 3 are needed for without swap
    freq=[[k,v] for k,v in Counter(nums).items()]
    perm=[]
    # find_perm()
    return all_perm

# 7. https://leetcode.com/problems/word-search/description/
def exist(self, board: List[List[str]], word: str) -> bool:
    # T: O(n*m*(4^w) and S:O(w) where w is length of word   
    # check at each board pos i,j for word
    # if the letter matches mark the board[i][j] and move to next 4 directions, when combing back unmark it
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

# 8. https://leetcode.com/problems/palindrome-partitioning/
def partition(self, s: str) -> List[List[str]]:
    # T:O(n*2^n) and S:O(n)
    def check_pal(i,j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def find_partition(index):
        if index==len(s):
            all_parts.append(cur_parts[:])
        else:
            for i in range(index,len(s)):
                if check_pal(index,i):
                    cur_parts.append(s[index:i+1])
                    find_partition(i+1)
                    cur_parts.pop()

    all_parts=[]
    cur_parts=[] 
    find_partition(0)           
    return all_parts

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

# 10. https://leetcode.com/problems/n-queens/
def solveNQueens(self, n: int) -> List[List[str]]:
    # T:O(n!) and S:O(n^2) for board
    def is_possible_to_place(i,j):
        return cols[j] and main_dig[j-i+n-1] and other_dig[j+i]

    def set_pos(i,j,with_queen=False):
        cols[j] = main_dig[j-i+n-1] = other_dig[j+i]= False if with_queen else True
        board[i][j]='Q' if with_queen else '.'

    def find_placings(i):
        if i==n:
            all_comb.append(["".join(row) for row in board])
        else:
            # try to place queen at each column of row i
            for j in range(n):
                if is_possible_to_place(i,j):
                    set_pos(i,j,with_queen=True) #place the queen
                    find_placings(i+1)
                    set_pos(i,j,with_queen=False) #unplace the queen
    
    cols=[True]*n
    main_dig=[True]*(2*n-1) # j-i+n-1
    other_dig=[True]*(2*n-1) # j+i
    all_comb=[]
    board = [list("." * n) for _ in range(n)]
    find_placings(0)
    return all_comb

# 11. https://leetcode.com/problems/generate-parentheses/description/
def generateParenthesis(self, n: int) -> List[str]:
    # T:O(4^n/sqrt(n)) and S:O(n)
    def find_paranthesis(left,right):
        if left==right==n:
            all_combs.append("".join(cur))
            return 
        # if left bracket is remaining use it
        if left<n:
            cur.append('(')
            find_paranthesis(left+1,right)
            cur.pop()
        # if left bracket more than right then we can close it, and it is valid
        if left>right:
            cur.append(')')
            find_paranthesis(left,right+1)
            cur.pop()

    cur=[]
    all_combs=[]
    find_paranthesis(0,0)
    return all_combs
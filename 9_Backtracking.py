from typing import List
from collections import Counter


# 1. https://leetcode.com/problems/subsets/
def subsets(self, nums: List[int]) -> List[List[int]]:
    # T:O(2^n) and S:O(n) T:O(n*2^n) if we consider the time to copy the subset to all_subsets as well

    def find_subset(index):
        if index == len(nums):
            all_subsets.append(cur_set[:])
            return

        # ignore current index
        find_subset(index + 1)
        # chooses the current index
        cur_set.append(nums[index])  # use it in cur subset
        find_subset(index + 1)
        cur_set.pop() # remove it from cur subset to as all combinations with num[index] in subset are already explored in above call

    all_subsets = []
    cur_set = []
    find_subset(0)
    return all_subsets

# 2. https://leetcode.com/problems/subsets-ii/
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    # T:O(2^n) and S:O(n) => T:(n*2^n) if we consider the time to copy the subset to all_subsets as well
    
    def find_subset(index):
        if index == len(freq_list):
            all_subsets.append(cur_subset[:])
        else:
            # ignore current index
            find_subset(index + 1)
            # ** use current index, if the number of items are still left and remain at same index
            if freq_list[index][1] > 0:
                freq_list[index][1] -= 1
                cur_subset.append(freq_list[index][0])
                find_subset(index)
                freq_list[index][1] += 1
                cur_subset.pop()

    # freq list, each element is [num, freq] and we will use the freq to decide how many times we can use the num in subset
    freq_list = [[k, v] for k, v in Counter(nums).items()]
    cur_subset = []
    all_subsets = []
    find_subset(0)
    return all_subsets


# 3. https://leetcode.com/problems/combination-sum/
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # T:O(2^(n)) and S:O(n)
    def dfs(idx, target):
        if target == 0:
            all_comb.append(cur_comb[:])
            return
        if idx == len(candidates):
            return

        # **numbers are sorted all nums at >=idx are greater than target so can't be used
        if candidates[idx] > target:
            return

        # skip cur idx
        dfs(idx + 1, target)
        # choose cur idx and remain at same index to choose again
        cur_comb.append(candidates[idx])
        dfs(idx, target - candidates[idx]) 
        cur_comb.pop()

    candidates.sort()
    cur_comb = []
    all_comb = []
    dfs(0, target)
    return all_comb

# 4. https://leetcode.com/problems/combination-sum-ii/
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # T:O(2^(n)) and S:O(n)
    def dfs(idx,target):
        if target==0:
            all_comb.append(cur_comb[:])
            return
        if idx==len(freq):
            return 
        
        # ** numbers are sorted all nums at >=idx are greater than target so can't be used
        if freq[idx][0] > target: 
            return 

        # skip cur idx
        dfs(idx+1,target)
        # choose cur idx if there are still some left, and remain at same index to choose again
        if freq[idx][1]>0:
            cur_comb.append(freq[idx][0])
            freq[idx][1]-=1
            dfs(idx,target-freq[idx][0])
            freq[idx][1]+=1
            cur_comb.pop()
    
    freq=[[k,v] for k,v in Counter(candidates).items()]
    freq.sort()
    cur_comb=[]
    all_comb=[]
    dfs(0,target)
    return all_comb


# 5. https://leetcode.com/problems/permutations/
def permute(self, nums: List[int]) -> List[List[int]]:
    # T:O(n*n!) and S:O(n) n! permutations and n for each perm to copy to all_perm
    def dfs(idx): #set num at pos idx
        if idx==n:
            all_perms.append(nums[:])
            return
        
        # for all nums idx to n, try all of them
        for i in range(idx,n):
            nums[idx],nums[i]=nums[i],nums[idx] #swap nums
            dfs(idx+1) #idx is set go for next index
            nums[idx],nums[i]=nums[i],nums[idx] #swap back to same state

    n=len(nums)
    all_perms=[]
    dfs(0)
    return all_perms

# 6. https://leetcode.com/problems/permutations-ii/
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # T:O(n*n!) and S:O(n) n! permutations and n for each perm to copy to all_perm    
    def dfs(idx): #set num at pos idx
        if idx==n:
            all_perms.append(nums[:])
            return
        
        # for all nums idx to n, try all of them
        seen=set()
        for i in range(idx,n):
            if nums[i] not in seen: #don't try all permutations by setting same no twice at idx
                seen.add(nums[i])
                nums[idx],nums[i]=nums[i],nums[idx] #swap nums
                dfs(idx+1) #idx is set go for next index
                nums[idx],nums[i]=nums[i],nums[idx] #swap back to same state

    n=len(nums)
    all_perms=[]
    dfs(0)
    return all_perms


# 7. https://leetcode.com/problems/word-search/description/
def exist(self, board: List[List[str]], word: str) -> bool:
    # T: O(n*m*(4^w) and S:O(w) where w is length of word
    def dfs(i,j,idx):
        if idx==len(word): # Found the word
            return True
        if not (0<=i<n and 0<=j<m) or (i,j) in visited or word[idx]!=board[i][j]: # skip all invalid cases
            return False
        
        visited.add((i,j)) # mark the board[i][j] as visited
        for dx,dy in directions: # Try all 4 directions 
            if dfs(i+dx,j+dy,idx+1):
                return True
        visited.discard((i,j)) # unmark the board[i][j] as visited to use it in other combinations as well

    visited=set()
    n,m=len(board),len(board[0])
    directions=[[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(n):
        for j in range(m):
            if dfs(i,j,0):
                return True
    return False

# 8. https://leetcode.com/problems/palindrome-partitioning/
def partition(self, s: str) -> List[List[str]]:
    # T:O(n*2^n) and S:O(n)
    # Time: O(n^2 * 2^(n-1)) ≈ O(n^2 * 2^n) — there are n-1 possible cut positions giving 2^(n-1) partition choices,
    # and for each state we may try O(n) substrings with each palindrome check costing O(n).
    def check_pal(i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def find_partition(index):
        if index == len(s): # reached end => one valid partition found
            all_parts.append(cur_parts[:])
            return

        # try every possible substring starting at index
        for i in range(index, len(s)):
            if check_pal(index, i): 
                cur_parts.append(s[index : i + 1]) # add the palindrome from index to i to current partition
                find_partition(i + 1) # look from i+1 for remaining partition
                cur_parts.pop()

    all_parts = []
    cur_parts = []
    find_partition(0)
    return all_parts


# 9. https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations(self, digits: str) -> List[str]:
    # T:O(4^n) and S:O(n)
    # We have 4 choices for each digit and n digits so 4^n combinations, and n for each combination to copy to all_combs as well, so T:O(n*4^n)
    def dfs(idx):
        if idx==len(digits):
            all_combs.append("".join(cur))
            return
        
        for c in mapping[int(digits[idx])]:
            cur.append(c)
            dfs(idx+1)
            cur.pop()

    mapping=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    all_combs=[]
    cur=[]
    dfs(0)
    return all_combs
    
# 10. https://leetcode.com/problems/n-queens/
def solveNQueens(self, n: int) -> List[List[str]]:
    # Time: O(N!) — each row chooses among remaining valid columns, leading to at most N! placements.
    # Space: O(N) for recursion stack and column/diagonal tracking.
    def dfs(row):
        if row==n:
            new_board=["".join(board[i]) for i in range(n)]
            all_comb.append(new_board)
            return
        
        for col in range(n):
            # check we can put queen in [row,col] location
            if col_check[col] and left_dig[row+col] and right_dig[row-col+n-1]:
                col_check[col] = left_dig[row+col] = right_dig[row-col+n-1] = 0 # mark the column and diagonals as not available for next rows
                board[row][col]='Q' # place the queen and go for next row
                dfs(row+1)
                board[row][col]='.' # unplace the queen and mark the column and diagonals as available
                col_check[col] = left_dig[row+col] = right_dig[row-col+n-1] = 1

    col_check=[1]*n
    left_dig=[1]*(2*n-1)
    right_dig=[1]*(2*n-1)
    all_comb=[]
    board=[['.']*n for _ in range(n)]
    dfs(0)
    return all_comb

# 11. https://leetcode.com/problems/generate-parentheses/description/
def generateParenthesis(self, n: int) -> List[str]:
    """
    Correct: T:O(4^n/sqrt(n)) and S:O(n) auxiliary (recursion + current path), excluding output.
    
    from basic recursion: 2^2n = 4^n as we have 2n positions and at each position we have 2 choices
    
    Time:   O(Cn * n), where Cn is the nth Catalan number (number of valid parentheses strings).
            Since Cn ≈ 4^n / (n^(3/2)), time can also be written as O(4^n / sqrt(n)).
    """

    def dfs(left, right):
        if left == right == n: #computed one valid Parentheses
            all_combs.append("".join(cur))
            return

        # if left still remaining, choose it and generate from it
        if left < n:
            cur.append("(")
            dfs(left + 1, right)
            cur.pop()

        # if left>right, choose right as it is valid and generate from it
        if left > right:
            cur.append(")")
            dfs(left, right + 1)
            cur.pop()

    cur = []
    all_combs = []
    dfs(0, 0)
    return all_combs


# ################## Hard Problems ###################


# 1.  https://leetcode.com/problems/permutation-sequence/description/
def getPermutation(n: int, k: int) -> str:
    fact = [1] * n
    for i in range(1, n):
        fact[i] = fact[i - 1] * i

    k -= 1  # make it 0th indexed
    kth_perm = ""
    nums = [str(i) for i in range(1, n + 1)]

    while n:
        n -= 1  # compute this factorial
        index_to_use = k // fact[n]
        k = k % fact[n]
        kth_perm += nums[index_to_use]
        nums.pop(index_to_use)  # this number is already used in perm

    return kth_perm

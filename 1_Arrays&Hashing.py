from typing import List 
from collections import defaultdict, Counter
import heapq 

# 1. https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(self, nums: List[int]) -> bool:
    # T:O(n) and S:O(n) for set
    seen=set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# 2. https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
    # T:O(n) and S:O(n) for freq dictionary
    if len(s) != len(t):
        return False
    freq = defaultdict(int)
    for i in range(len(s)):
        freq[s[i]]+=1
        freq[t[i]]-=1

    return all(v==0 for v in freq.values())

# 3. https://leetcode.com/problems/two-sum/description/
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # T:O(n) and S:O(n) for index_of_num dictionary
    index_of_num={}
    for i in range(len(nums)):
        if target-nums[i] in index_of_num:
            return [index_of_num[target-nums[i]],i]
        index_of_num[nums[i]]=i

# 4. https://leetcode.com/problems/group-anagrams/description/
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # T:O(n) and S:O(n) for dictionary
    def create_hash_key(word):
        freq = [0] * 26  # Assuming input consists of lowercase English letters
        for c in word:
            freq[ord(c) - ord('a')] += 1
        # Create a unique signature using the character frequencies
        hash_key = tuple(freq)
        return hash_key
    
    d = defaultdict(list)
    for word in strs:
        d[create_hash_key(word)].append(word)
    return list(d.values())


# 5. https://leetcode.com/problems/top-k-frequent-elements/description/
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # T:O(nlogk) and S:O(n) for freq dictionary
    freq=Counter(nums)
    min_heap=[] # use min_heap to have the max_freq at the end of heap
    for key,value in freq.items():
        heapq.heappush(min_heap,(value,key)) # push (priority, value) in heap
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    
    return [item[1] for item in min_heap]

# 6. https://neetcode.io/problems/string-encode-and-decode
class EndodeAndDecode:
    def encode(self, strs: List[str]) -> str:
        # T:O(n) and S:O(1)
        encoded=""
        for s in strs:
            encoded+=f"{len(s)}:{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        # T:O(n) and S:O(1)
        decoded=[]
        i=0
        while i <len(s):
            str_size=""
            while s[i]!=":":
                str_size+=s[i]
                i+=1
            str_size=int(str_size)
            i=i+1 # will move to start of string after ":"
            j=i+str_size # will have the end of string +1 position
            decoded.append(s[i:j])
            i=j
        return decoded



# 7. https://leetcode.com/problems/product-of-array-except-self/description/
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # T:O(n) and S:O(1) excluding the ans array
    prefix_mul=[]
    pre=1
    # prefix_mul at ith index will have nums[0]*nums[1]..*nums[i-1]
    for num in nums:
        prefix_mul.append(pre)
        pre*=num
    suf=1
    # ans[i]=pref[i]*suf, i.e 0 to i-1 and i+1 to n-1
    for i in range(len(nums)-1,-1,-1):
        prefix_mul[i]=prefix_mul[i]*suf
        suf*=nums[i]
    return prefix_mul
    
# 8. https://leetcode.com/problems/valid-sudoku/description/
class CheckSudoku:
    # T:O(n*n) and S:O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_row_and_col_valid(pos):
            present_in_row, present_in_col=set(),set()
            for i in range(9):
                # check pos row
                if board[pos][i]!='.' and board[pos][i] in present_in_row:
                    return False
                # check pos col
                if board[i][pos]!='.' and board[i][pos] in present_in_col:
                    return False
                present_in_row.add(board[pos][i])
                present_in_col.add(board[i][pos])
            return True
        
        def is_matrix_valid(row,col):
            present=set()
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j]!='.' and board[i][j] in present:
                        return False
                    present.add(board[i][j])
            return True
        
        for i in range(9):
            if not is_row_and_col_valid(i):
                return False
        for i in range(3):
            for j in range(3):
                if not is_matrix_valid(i*3,j*3):
                    return False
        return True

# 9. https://leetcode.com/problems/longest-consecutive-sequence/description/
def longestConsecutive(self, nums: List[int]) -> int:
    # T:O(n) and S:O(n) for set
    present=set(nums)
    ans=0
    for n in present:
        if n-1 in present:
            continue
        end = n
        while end+1 in present:
            end+=1
        ans=max(ans,end-n+1)
    return ans
            
# 10. https://leetcode.com/problems/count-number-of-bad-pairs/description/
def countBadPairs(self, nums: List[int]) -> int:
    # T:O(n) and S:O(n) for defaultdict
    good_pairs=0
    count=defaultdict(int)
    for i, num in enumerate(nums):
        good_pairs+=count[num-i]
        count[num-i]+=1
    n=len(nums)
    #Wrong: I was using (n*(n+1))//2 for total pairs, nC2 is n*(n-1)//2
    total_pairs=(n*(n-1))//2
    bad_pairs=total_pairs-good_pairs
    return bad_pairs


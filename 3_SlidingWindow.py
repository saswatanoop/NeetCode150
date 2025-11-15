from typing import List
from collections import defaultdict
from collections import Counter
from collections import deque

# 1. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def maxProfit( prices: List[int]):
    # T:O(n) and S:O(1)
    max_profit=0
    min_stock_value=float("inf")
    # we will try to sell each day with maximum profit and use the best day 
    for price in prices:
        max_profit=max(max_profit,price-min_stock_value)
        min_stock_value=min(min_stock_value,price)
    return max_profit

# 2. https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Keep adding to window as soon as it becomes invalid, start removing from start of window to make it valid
def lengthOfLongestSubstring( s: str) -> int:
    # T:O(n) and S:O(n) for freq dictionary
    start = end = 0
    max_len = 0
    seen = set()

    while end < len(s):
        # shrink window if duplicate found
        while s[end] in seen:
            seen.remove(s[start])
            start += 1

        # include current character
        seen.add(s[end])
        max_len = max(max_len, end - start + 1)
        end += 1

    return max_len

# 3. https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement_with_extra_26_iteration(self, s: str, k: int) -> int:
        # T:O(n*26) and S:O(n) for freq dictionary
        start=end=0
        ans=0
        freq=defaultdict(int)
        while end<len(s):
            freq[s[end]]+=1
            # make the window valid so that at max k replacements are needed
            while end-start+1-max(freq.values())>k:
                freq[s[start]]-=1
                start+=1
            ans=max(ans,end-start+1)
            end+=1

        return ans

    def characterReplacement(self, s: str, k: int) -> int:
        # T:O(n) and S:O(n) for freq dictionary
        start=end=0
        ans=0
        freq=defaultdict(int)
        max_freq_value=0
        while end<len(s):
            freq[s[end]]+=1
            max_freq_value=max(max_freq_value,freq[s[end]])
            
            # once we have a valid window, we will keep the window size same or increase it, never decrease it
            while end-start+1-max_freq_value>k:
                freq[s[start]]-=1
                start+=1
            
            ans=max(ans,end-start+1)
            end+=1

        return ans

# 4. https://leetcode.com/problems/permutation-in-string/description/
def checkInclusion(self, s1: str, s2: str) -> bool:
    # T:O(n) and S:O(n) for freq dictionary
    '''
    Cases: 
    1. char is not in s1 whole window is invalid, add all elements back to freq from that windows
    2. char is in freq but freq is already 0, then remove from left till freq of char==1, so that it can be added
    '''
    if len(s1)>len(s2):
        return False
    
    freq=Counter(s1)
    
    start=end=0
    while end<len(s2):
        # char is not in s1, clear out the whole window
        if s2[end] not in freq:
            while start!=end:
                freq[s2[start]]+=1
                start+=1
            start=end=end+1
        # char is part of s1 and window can be valid
        else:
            while freq[s2[end]]==0:
                freq[s2[start]]+=1
                start+=1
            freq[s2[end]]-=1
            if len(s1)==end-start+1:
                return True
            end+=1
    return False

# 5. https://leetcode.com/problems/minimum-window-substring/description/
def minWindow( s: str, t: str) -> str:
    # T:O(n) and S:O(n) for freq dictionary
    # 1. find a valid window first with all chars in t
    # 2. Once found, remove from left as much as possible and keep window valid  
    if len(t)>len(s):
        return ""
    
    freq=Counter(t)
    rem=len(t)
    res=None
    
    start=end=0
    while end<len(s):
        if s[end] in freq:
            if freq[s[end]]>0:
                rem-=1
            freq[s[end]]-=1
        
        if rem==0:
            # Mistake: if the char is not part of freq then also we need to remove it from left side
            while s[start] not in freq or freq[s[start]]<0:
                if s[start] in freq:
                    freq[s[start]]+=1
                start+=1
            if res is None or len(res)>end-start+1:
                res=s[start:end+1]  
        end+=1
    
    return res if res else ""

# 6. https://leetcode.com/problems/sliding-window-maximum/description/
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # T:O(n) and S:O(n) for deque
    deq=deque() # will store index, and maintain nums[index] in decreasing order of value
    ans=[]

    for i in range(len(nums)):

        # remove the out of window elements from left, using index stored in deq
        # size k=2 end=3 then 3-2=1, allowed are 2 and 3, so allowed >= end-k+1 
        while deq and deq[0]<=i-k:
            deq.popleft()
        # add element from the right, and maintain decreasing order
        while deq and nums[deq[-1]]<=nums[i]:
            deq.pop()
        deq.append(i)
        
        # add to the answers, if k size window is ready
        if i>=k-1:
            ans.append(nums[deq[0]])

    
    return ans
        
from typing import List
from collections import defaultdict
from collections import Counter
from collections import deque

# 1. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def maxProfit( prices: List[int]) -> int:
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
    win_s=win_e=0
    ans=0
    freq=defaultdict(int)

    while win_e<len(s):
        freq[s[win_e]]+=1 # add to window
        # shrink window from left till the window is invalid
        while freq[s[win_e]]>1:
            freq[s[win_s]]-=1
            win_s+=1
        ans=max(ans,win_e-win_s+1)
        win_e+=1
    
    return ans

# 3. https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement_with_extra_26_iteration(self, s: str, k: int) -> int:
        # T:O(n*26) and S:O(n) for freq dictionary
        wins=wine=0
        ans=0
        freq=defaultdict(int)
        while wine<len(s):
            freq[s[wine]]+=1
            # make the window valid so that at max k replacements are needed
            while wine-wins+1-max(freq.values())>k:
                freq[s[wins]]-=1
                wins+=1
            ans=max(ans,wine-wins+1)
            wine+=1

        return ans

    def characterReplacement(self, s: str, k: int) -> int:
        # T:O(n) and S:O(n) for freq dictionary
        wins=wine=0
        ans=0
        freq=defaultdict(int)
        max_freq_value=0
        while wine<len(s):
            freq[s[wine]]+=1
            max_freq_value=max(max_freq_value,freq[s[wine]])
            # once we have a valid window, we will keep the window size same or increase it, never decrease it
            while wine-wins+1-max_freq_value>k:
                freq[s[wins]]-=1
                wins+=1
            ans=max(ans,wine-wins+1)
            wine+=1

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

    wins=wine=0

    while wine<len(s2):
        if s2[wine] not in freq:
            while wins!=wine:
                freq[s2[wins]]+=1
                wins+=1
            wins=wine=wine+1
            
        else:
            while freq[s2[wine]]==0:
                freq[s2[wins]]+=1
                wins+=1
            freq[s2[wine]]-=1
            if len(s1)==wine-wins+1:
                return True
            wine+=1
    return False

# 5. https://leetcode.com/problems/minimum-window-substring/description/
def minWindow( s: str, t: str) -> str:
    # T:O(n) and S:O(n) for freq dictionary
    # 1. find a valid window first with all chars in t
    # 2. Once found, remove from left as much as possible and keep window valid  
    wins=wine=0
    freq=Counter(t)
    rem=len(t)
    res=None
    while wine<len(s):
        if s[wine] in freq:
            if freq[s[wine]]>0:
                rem-=1
            freq[s[wine]]-=1
        
        if rem==0:
            # Mistake: if the char is not part of freq then also we need to remove it from left side
            while s[wins] not in freq or freq[s[wins]]<0:
                if s[wins] in freq:
                    freq[s[wins]]+=1
                wins+=1
            if res is None or len(res)>wine-wins+1:
                res=s[wins:wine+1]  
        wine+=1
    
    return res if res else ""

# 6. https://leetcode.com/problems/sliding-window-maximum/description/
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # T:O(n) and S:O(n) for deque
    wine=0
    deq=deque() # will store index, and maintain nums[index] in decreasing order of value
    ans=[]

    while wine<len(nums):

        # remove the out of window elements from left, using index stored in deq
        # size k=2 wine=3 then 3-2=1, allowed are 2 and 3, so allowed >= wine-k+1 
        while deq and deq[0]<=wine-k:
            deq.popleft()
        # add element from the right, and maintain decreasing order
        while deq and nums[deq[-1]]<=nums[wine]:
            deq.pop()
        deq.append(wine)
        
        # add to the answers, if k size window is ready
        if wine>=k-1:
            ans.append(nums[deq[0]])
        wine+=1
    
    return ans
        
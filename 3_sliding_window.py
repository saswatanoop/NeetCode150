from typing import List
from collections import defaultdict
from collections import Counter
from collections import deque

# 1. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def maxProfit(self, prices: List[int]) -> int:
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
def lengthOfLongestSubstring(self, s: str) -> int:
    # T:O(n) and S:O(n) for freq dictionary
    win_s=win_e=0
    ans=0
    freq=defaultdict(int)

    while win_e<len(s):
        freq[s[win_e]]+=1
        while freq[s[win_e]]>1:
            freq[s[win_s]]-=1
            win_s+=1
        ans=max(ans,win_e-win_s+1)
        win_e+=1
    
    return ans

# 5. https://leetcode.com/problems/minimum-window-substring/description/
def minWindow(self, s: str, t: str) -> str:
    # T:O(n) and S:O(n) for freq dictionary
    # 1. find a valid window first with all chars in t
    # 2. Once found, remove from left as much as possible and keep window valid  
    wins=wine=0
    freq=Counter(t)
    gs=ge=-1
    rem=len(t)
    while wine<len(s):
        if s[wine] in freq:
            if freq[s[wine]]>0:
                rem-=1
            freq[s[wine]]-=1
        
        if rem==0:
            while s[wins] not in freq or freq[s[wins]]<0:
                if s[wins] in freq:
                    freq[s[wins]]+=1
                wins+=1
            if gs==-1 or  ge-gs>wine-wins:
                gs,ge=wins,wine
        wine+=1
    
    return "" if gs==-1 else s[gs:ge+1]



# 6. https://leetcode.com/problems/sliding-window-maximum/description/
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # T:O(n) and S:O(n) for deque
    wine=0
    deq=deque() # will store index, and maintain nums[index] in decreasing order of value
    ans=[]

    while wine<len(nums):

        # remove the out of window elements from left, using index stored in deq
        while deq and wine-k>=0 and deq[0]<=wine-k:
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
        
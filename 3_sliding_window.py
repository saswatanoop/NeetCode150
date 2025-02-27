from typing import List
from collections import defaultdict

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
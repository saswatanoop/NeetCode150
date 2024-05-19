#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <list>
#include <sstream>
#include <climits>
#include <unordered_set>

using namespace std;

/*
1. Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
2. Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
6. Sliding Window Maximum: https://leetcode.com/problems/sliding-window-maximum/description/
*/

// 1
class BuyAndSellStock
{
    /*
        We will try to sell each day with max profit possible, and return the global max
        Profit[i]= Price[i]-minPriceTill[i-1],  0 when the differnece is negative
        T:O(n) S:O(1)
    */
public:
    int maxProfit(vector<int> &prices)
    {
        int prof = 0;
        int minV = prices[0]; // to store lowest price we can buy till Ith day
        for (int i = 1; i < prices.size(); i++)
        {
            prof = max(prof, prices[i] - minV); // max profit we can make if we sell today
            minV = min(minV, prices[i]);        // update min buying price
        }
        return prof;
    }
};

// 2
class LongestSubstring
{
    /*
        We will use sliding window approach, keep adding from right till you see an existing character
        once existing character is there remove from left till it is not present
        T:O(n) S:O(1)
    */
public:
    int lengthOfLongestSubstring(string s)
    {
        int n = s.size();
        int winStart = 0, winEnd = 0;
        int maxSubstrSize = 0;
        unordered_set<char> char_exist;

        while (winEnd < n)
        {
            // we need to remove from left till current char is not present in window
            while (char_exist.find(s[winEnd]) != char_exist.end())
            {
                char_exist.erase(s[winStart]);
                winStart++;
            }
            // now insert the char since it is not present in window
            char_exist.insert(s[winEnd]);
            maxSubstrSize = max(maxSubstrSize, winEnd - winStart + 1); // now the window has only unique characters
            winEnd++;
        }
        return maxSubstrSize;
    }
};

// 6
class MaxSlidingWindow
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        deque<int> deq;
        vector<int> maxValeusInWindow;
        for (int i = 0; i < k - 1; i++)
        {
            while (!deq.empty() && nums[i] >= nums[deq.back()])
                deq.pop_back();
            deq.push_back(i);
        }
        for (int i = k - 1; i < nums.size(); i++)
        {
            while (!deq.empty() && nums[i] >= nums[deq.back()])
                deq.pop_back();
            deq.push_back(i);

            // check the window size is of size k from left as well
            while (deq.front() + k == i)
                deq.pop_front();
            maxValeusInWindow.push_back(nums[deq.front()]);
        }
        return maxValeusInWindow;
    }
};

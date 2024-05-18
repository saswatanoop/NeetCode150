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

*/
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
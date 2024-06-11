#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <sstream>
#include <climits>
#include <unordered_set>

using namespace std;
/*
1. Subsets: https://leetcode.com/problems/subsets/description/
*/

class AllSubsets
{
    void subsets_helper(vector<int> &nums, int pos, vector<int> &subset, vector<vector<int>> &all_subsets)
    {
        // all the elements in nums have been processed
        if (pos == nums.size())
        {
            all_subsets.push_back(subset);
            return;
        }
        // don't take nums[pos] element
        subsets_helper(nums, pos + 1, subset, all_subsets);

        // take nums[pos] element
        subset.push_back(nums[pos]);
        subsets_helper(nums, pos + 1, subset, all_subsets);
        subset.pop_back(); // don't forget to remove it
    }

public:
    vector<vector<int>> subsets_iter(vector<int> &nums)
    {
        vector<vector<int>> ans;
        ans.push_back({});
        for (auto v : nums)
        {
            vector<vector<int>> temp;
            for (auto subset : ans)
            {
                temp.push_back(subset);
                subset.push_back(v);
                temp.push_back(subset);
            }
            ans = temp;
        }
        return ans;
    }
    vector<vector<int>> subsets(vector<int> &nums)
    {
        if (nums.size() == 0)
            return {};

        vector<vector<int>> all_subsets = {};
        vector<int> subset = {};
        subsets_helper(nums, 0, subset, all_subsets);
        return all_subsets;
    }
};
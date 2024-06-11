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
2. Subsets II: https://leetcode.com/problems/subsets-ii/description/
3. Combination Sum: https://leetcode.com/problems/combination-sum/description/
*/

// 1
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

// 2
class AllUniqueSubsetsWithDuplicates
{
public:
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        vector<vector<int>> ans;
        vector<int> subset;
        vector<pair<int, int>> freq;
        unordered_map<int, int> count;
        for (auto v : nums)
            count[v]++;
        // we will use freq vector instead of original nums vector and follow same logic as subsets
        for (auto p : count)
            freq.push_back(p);

        subsetsWithDup_helper(freq, 0, subset, ans);
        return ans;
    }
    void subsetsWithDup_helper(vector<pair<int, int>> &freq, int pos, vector<int> &subset, vector<vector<int>> &ans)
    {
        // we have processed all the elements
        if (pos == freq.size())
        {
            ans.push_back(subset);
            return;
        }

        // do not take it, all the cases where the current is not in subset
        subsetsWithDup_helper(freq, pos + 1, subset, ans);

        // take current if atleast 1 item is still present
        if (freq[pos].second > 0)
        {
            subset.push_back(freq[pos].first);
            // so it can be used at max remaining number of times
            freq[pos].second--;
            subsetsWithDup_helper(freq, pos, subset, ans);
            freq[pos].second++;
            subset.pop_back();
        }
    }
};

// 3
class CombinationSum
{
public:
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        vector<vector<int>> all_combinations = {};
        vector<int> combination = {};
        combinationSum_helper(candidates, 0, target, combination, all_combinations);
        return all_combinations;
    }
    void combinationSum_helper(vector<int> &candidates, int pos, int target,
                               vector<int> &combination, vector<vector<int>> &all_combinations)
    {
        // we got one possible combination
        if (target == 0)
        {
            all_combinations.push_back(combination);
            return;
        }
        if (pos >= candidates.size())
            return;

        // do not take current
        combinationSum_helper(candidates, pos + 1, target, combination, all_combinations);

        // take current if it's value <= target
        if (candidates[pos] <= target)
        {
            combination.push_back(candidates[pos]);
            // pos will remain as it is, since we can take this item again
            combinationSum_helper(candidates, pos, target - candidates[pos], combination, all_combinations);
            combination.pop_back();
        }
    }
};
//
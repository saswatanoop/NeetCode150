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
4. Combination Sum II: https://leetcode.com/problems/combination-sum-ii/description/
7. Word Search: https://leetcode.com/problems/word-search/description/
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
        // we have processed all the elements and did not find a combination
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

// 4
class CombinationSum2
{
public:
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
    {
        vector<vector<int>> ans;
        vector<int> combination;
        unordered_map<int, int> count;
        vector<pair<int, int>> freq;
        for (auto v : candidates)
            count[v]++;
        // we will use freq vector instead of original nums vector and follow same logic as combination sum
        for (auto p : count)
            freq.push_back(p);
        combinationSum_helper(freq, 0, target, combination, ans);
        return ans;
    }
    void combinationSum_helper(vector<pair<int, int>> &freq, int pos, int target,
                               vector<int> &combination, vector<vector<int>> &ans)
    {
        // we got one possible combination
        if (target == 0)
        {
            ans.push_back(combination);
            return;
        }
        // we have processed all the elements and did not find a combination
        if (pos >= freq.size())
            return;

        // take current: if it's value <= target and it's freq is there
        if (freq[pos].first <= target && freq[pos].second > 0)
        {
            combination.push_back(freq[pos].first);
            freq[pos].second--;
            // keep the pos same, we might use same number again if it's freq is still >0
            combinationSum_helper(freq, pos, target - freq[pos].first, combination, ans);
            freq[pos].second++;
            combination.pop_back();
        }
        // do not take current
        combinationSum_helper(freq, pos + 1, target, combination, ans);
    }
};

// 7
class WordSearch
{
public:
    bool exist(vector<vector<char>> &board, string word)
    {
        for (int i = 0; i < board.size(); i++)
            for (int j = 0; j < board[0].size(); j++)
                if (search(board, i, j, word, 0))
                    return true;
        return false;
    }
    bool search(vector<vector<char>> &board, int i, int j, string word, int pos)
    {
        // all the letters have been matched already
        if (pos == word.size())
            return true;

        // out of range, alrady visited or word[index] is different
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] == '.' || board[i][j] != word[pos])
            return false;

        auto last = board[i][j];
        board[i][j] = '.'; // mark i,j as visited

        bool found = false;
        int dx[] = {0, 0, -1, 1};
        int dy[] = {1, -1, 0, 0};
        for (int k = 0; k < 4; k++)
            if (search(board, i + dx[k], j + dy[k], word, pos + 1))
            {
                found = true; // can' return true here since we need to correct the board before returning
                break;
            }

        board[i][j] = last; // reset the board
        return found;
    }
};
//
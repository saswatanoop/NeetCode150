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
1. Contains Duplicate :https://leetcode.com/problems/contains-duplicate/description/
2. Valid Anagram: https://leetcode.com/problems/valid-anagram/description/
3. Two Sum: https://leetcode.com/problems/two-sum/description/
4. Group Anagrams: https://leetcode.com/problems/group-anagrams/description/
*/

// 1.
class ContainsDuplicate
{
    /*
    1. For sorted array : no need for set, compare i and i-1 index values, if same there is duplicate
        T: O(n) S:O(1)

    2. For unsorted array: use hashmap/set
        T: O(n) S:O(n)
    */
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> s;
        for (auto v : nums)
        {
            if (s.find(v) != s.end())
                return true;
            s.insert(v);
        }
        return false;
    }
};

// 2.
class IsAnagram
{
    /*
        T:O(n) S:O(26)=>O(1)
    */
public:
    bool isAnagram(string s, string t)
    {
        // check number of characters are same in both strings first
        if (s.size() != t.size())
            return false;

        // use vector as map since already know the characters are lowercase alphabets
        vector<int> freq(26, 0);

        // increase frq for first string and decrease for the other if all freqs 0 at end then anagram
        for (int i = 0; i < s.size(); i++)
        {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }

        for (auto v : freq)
            if (v != 0)
                return false;
        return true;
    }
};

// 3.
class TwoSum
{
    /*
        1. For Sorted array: use two pointers start and end
            T:O(n) S:O(1)

        2. For Unsorted array: use hashmap to store the index of each value
            we will check for nums[i] if target-nums[i] is already present
            T:O(n) S:O(n)
    */
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> value_to_index;
        for (int i = 0; i < nums.size(); i++)
        {
            if (value_to_index.find(target - nums[i]) != value_to_index.end())
                return {i, value_to_index[target - nums[i]]};
            value_to_index[nums[i]] = i;
        }
        return {};
    }
};

// 4.
class GroupAnagrams
{
    /*
        Number of strings: n, max size of each string: m
        1. Sort the strings and anagrams will be same after being sorted
            T:O(n*mlogm) S:O(nk)

        2. Do counting sort, saswat=> a2s2t1w1, anagrams will have same freq mapping
            T:O(nm) S:O(nm)
    */
private:
    string createFreqMap(const string &s)
    {
        vector<int> freq(26, 0);
        for (auto c : s)
            freq[c - 'a']++;

        string freqMap = "";
        for (int i = 0; i < 26; i++)
            if (freq[i] > 0)
                freqMap += char('a' + i) + to_string(freq[i]);
        return freqMap;
    }

public:
    // 1
    vector<vector<string>> groupAnagramsSortMethod(vector<string> &strs)
    {
        unordered_map<string, vector<string>> groups;

        for (int i = 0; i < strs.size(); i++)
        {
            string copy(strs[i]);
            sort(copy.begin(), copy.end());
            if (groups.find(copy) == groups.end())
                groups[copy] = {};
            groups[copy].push_back(strs[i]);
        }
        vector<vector<string>> ans;
        for (auto p : groups)
            ans.push_back(p.second);

        return ans;
    }
    // 2
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> groupedAnagrams;
        for (auto s : strs)
        {
            auto freqMap = createFreqMap(s);
            groupedAnagrams[freqMap].push_back(s);
        }
        for (auto p : groupedAnagrams)
            ans.push_back(p.second);
        return ans;
    }
};
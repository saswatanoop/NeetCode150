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
*/

// 1.
class ContainsDuplicate
{
    /*
    For sorted array : no need for set, compare i and i-1 index values, if same there is duplicate
        T: O(n) S:O(1)

    For unsorted array: use hashmap/set
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

// 2
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
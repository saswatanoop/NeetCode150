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
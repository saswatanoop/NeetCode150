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
1. Valid Palindrome :https://leetcode.com/problems/valid-palindrome/description/
2. Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
4. Container With Most Water :https://leetcode.com/problems/container-with-most-water/description/
5. Trapping Rain Water :https://leetcode.com/problems/trapping-rain-water/description/
*/

// 1.
class CheckPalindrome
{
public:
    bool isAlphaNumeric(char c)
    {
        return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z');
    }

    bool isPalindrome(string s)
    {
        int n = s.size();
        int i = 0, j = n - 1;
        while (i < j)
        {
            // i<j check very important in all 3 conditions
            while (i < j && !isAlphaNumeric(s[i]))
                i++;
            while (i < j && !isAlphaNumeric(s[j]))
                j--;
            if (i < j && tolower(s[i]) != tolower(s[j]))
                return false;

            i++;
            j--;
        }
        return true;
    }
};

// 2.
class TwoSumSortedArray
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {

        int i = 0, j = nums.size() - 1;

        while (i < j)
        {
            int sum = nums[i] + nums[j];
            if (sum == target)
                break;
            else if (sum > target)
                j--;
            else
                i++;
        }
        return {i + 1, j + 1};
    }
};

// 4.
class ContainerMaxWater
{
public:
    int maxArea(vector<int> &height)
    {
        int s = 0, e = height.size() - 1;
        int maxWaterInContainer = 0;

        while (s < e)
        {
            maxWaterInContainer = max(maxWaterInContainer, min(height[e], height[s]) * (e - s));
            if (height[s] < height[e])
                s++;
            else
                e--;
        }

        return maxWaterInContainer;
    }
};

// 5.
class TrapRainWater
{
public:
    int trap_extra_space(vector<int> &height)
    {
        int n = height.size();
        vector<int> left(n, 0), right(n, 0);

        int l_max = 0, r_max = 0;
        for (int i = 1; i < n; i++)
        {
            l_max = max(l_max, height[i - 1]);
            left[i] = l_max;

            r_max = max(r_max, height[n - i]);
            right[n - i - 1] = r_max;
        }
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            int water = max(min(left[i], right[i]) - height[i], 0);
            ans += water;
        }
        return ans;
    }
    int trap(vector<int> &height)
    {
        int l = 0, r = height.size() - 1;
        int lmax = 0, rmax = 0;
        int maxWater = 0;

        while (l <= r)
        {
            if (lmax < rmax)
            {
                maxWater += max(lmax - height[l], 0);
                lmax = max(lmax, height[l]);
                l++;
            }
            else
            {
                maxWater += max(rmax - height[r], 0);
                rmax = max(rmax, height[r]);
                r--;
            }
        }
        return maxWater;
    }
};

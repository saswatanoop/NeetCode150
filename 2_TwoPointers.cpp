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
3. 3Sum: https://leetcode.com/problems/3sum/description/
4. Container With Most Water :https://leetcode.com/problems/container-with-most-water/description/
5. Trapping Rain Water :https://leetcode.com/problems/trapping-rain-water/description/
*/

// 1.
class CheckPalindrome
{
    /*
        if the string only had alphanumneric we can move i and j from both the side, the main part of this to find the alphanumeric
        characters and then check if they are same
        T:O(n) S:O(1)
    */
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
    /*
        Too easy no need for explanation
        T:O(n) S:O(1)
    */
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

// 3.
class ThreeSum
{
    /*
        We don't want unique triplets of indexes, we want unique triplets of values,

        T:O(n^2): nlogn + n*(n-1)
        S:O(n) //the pairs returned by the twoSum function
    */
    vector<vector<int>> twoSum(vector<int> &nums, int s, int e, int target)
    {
        vector<vector<int>> twoSums;
        while (s < e)
        {
            int sum = nums[s] + nums[e];
            if (sum == target)
            {
                twoSums.push_back({nums[s], nums[e]});
                // num[s] and num[e] are used
                s++;
                e--;
                // search for new nums[s] value, we want unique pairs whose sum is target
                while (s < e && nums[s] == nums[s - 1])
                    s++;
            }
            else if (sum > target)
                e--;
            else
                s++;
        }
        return twoSums;
    }

public:
    vector<vector<int>>
    threeSum(vector<int> &nums)
    {
        int target = 0; // it is specified in problem target is 0
        vector<vector<int>> threeSums;
        sort(nums.begin(), nums.end());
        int s = 0, e = nums.size() - 1;
        while (s < e)
        {
            auto ans = twoSum(nums, s + 1, e, target - nums[s]);
            if (ans.size() > 0)
                for (auto v : ans)
                    threeSums.push_back({nums[s], v[0], v[1]});

            // nums[s] used,search for new nums[s] value, since all tiplets which has nums[s] are already added, and we need unique ones
            s++;
            while (s < e && nums[s - 1] == nums[s])
                s++;
        }
        return threeSums;
    }
};

// 4.
class ContainerMaxWater
{
    /*
        We will start from max width, with s=0 and e=n-1 and try to find max Water possible in container
        the vertical line which whose height is lower we will move it and try to use the long vertical line for max water
        T:O(n), S:O(1)
    */
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
    /*
        For each index the max water that can be trapped is = min(rmax,lmax)-height[index] if negative then 0
        T:O(n) S:O(1)

        1. With Extra space:
             we will store max height on the lefi of index i and right of index i and use it to find the ans

        2: Without extra space:
            we will keep two pointers at start and at end and will move the one whose side the max(lmax or rmax) is minimum
            since we can only store the min(lmax,rmax)-height[i] so just move that side which is lower
    */
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

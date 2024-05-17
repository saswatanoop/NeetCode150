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
4. Container With Most Water :https://leetcode.com/problems/container-with-most-water/description/
5. Trapping Rain Water :https://leetcode.com/problems/trapping-rain-water/description/
*/

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

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

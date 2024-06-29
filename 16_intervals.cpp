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
1. Insert Interval: https://leetcode.com/problems/insert-interval/
*/
class InsertInterval
{
    /*
        My old mistake: is to correctly check if there is a collision before I process the next interval

        No overlap: interval_x.end < interval_y.start
        Overlap: !(interval_x.end < interval_y.start)

        T:O(n) S:O(n)
    */
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> merged;

        // 1st phase: push intervals which do not have overlap with newInterval
        int i = 0, n = intervals.size();
        while (i < n && intervals[i][1] < newInterval[0])
            merged.push_back(intervals[i++]); // push interval if end of interval we are processing < start of new interval

        // 2nd phase: same as merge interval where last is newInterval
        while (i < n && !(newInterval[1] < intervals[i][0])) // notice the !, if newInterval[1]<intervals[i][0] there is no overlap
        {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        merged.push_back(newInterval);

        // 3rd phase: push intervals which do not have overlap after inserting interval
        while (i < n)
            merged.push_back(intervals[i++]);

        return merged;
    }
};
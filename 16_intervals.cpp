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
2. Merge Intervals: https://leetcode.com/problems/merge-intervals/description/
*/

// 1
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

// 2
class MergeIntervals
{
    /*
        1. Sort by start time and keep resolving the conflicts untill all intervals are processed
        T:O(nlogn) S:O(n)
    */
public:
    vector<vector<int>> merge_(vector<vector<int>> &intervals)
    {
        vector<vector<int>> merged;
        sort(intervals.begin(), intervals.end());
        auto last = intervals[0];

        for (int i = 1; i < intervals.size(); i++)
        {
            if (last[1] < intervals[i][0]) // no conflict
            {
                merged.push_back(last);
                last = intervals[i];
            }
            else // there is conflict merge them and set the correct end time
                last[1] = max(last[1], intervals[i][1]);
        }
        // push the last one
        merged.push_back(last);

        return merged;
    }
};

// 3

// 4

//
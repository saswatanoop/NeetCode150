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
Always clear that at boundary they are at conlfict or not example: [2,5] and [5,9], they may or may not be in conflict
depending on the problem

1. Insert Interval: https://leetcode.com/problems/insert-interval/
2. Merge Intervals: https://leetcode.com/problems/merge-intervals/description/
3. Non-overlapping Intervals: https://leetcode.com/problems/non-overlapping-intervals/description/
4. Meeting Rooms: https://neetcode.io/problems/meeting-schedule
5. Meeting Rooms II: https://neetcode.io/problems/meeting-schedule-ii
6. Minimum Interval to Include Each Query: https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
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
class NonOverLappingIntervals
{
    /*
        We will find the maximum number of activities we can do
        Min intervals to remove= totalActivities - maxActiviesPossible

        Sort in ascending order by end time
        T:O(nlogn) S:O(n)
    */
    static bool comp(vector<int> const &a, vector<int> const &b) { return a[1] < b[1]; }

public:
    int eraseOverlapIntervals(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end(), comp);
        int maxMeetings = 1;
        auto last = intervals[0];
        for (int i = 1; i < intervals.size(); i++)
        {
            // can do ith activity, increase the count
            if (last[1] <= intervals[i][0])
            {
                maxMeetings++;
                last = intervals[i];
            }
            // can't attend ith meeting, can store intervals to be erased here
            else
                continue;
        }
        return intervals.size() - maxMeetings;
    }
};

// 4
class Interval
{
public:
    int start, end;
    Interval(int start, int end)
    {
        this->start = start;
        this->end = end;
    }
};
class CheckAllMeetingsPossible
{
    /*
        Sort in increasing order of endTime and try to finish the meeting which finishes earlier
        T:O(nlogn) S:O(1)
    */
    static bool comp(const Interval &a, const Interval &b) { return a.end < b.end; }

public:
    bool canAttendMeetings(vector<Interval> &intervals)
    {
        if (intervals.size() <= 1)
            return true;

        // sort by the meeting which finishes first
        sort(intervals.begin(), intervals.end(), comp);

        auto last = intervals[0];
        for (int i = 1; i < intervals.size(); i++)
        {
            // can do the ith meeting
            if (last.end <= intervals[i].start)
                last = intervals[i];
            // can't do ith meeting, we can't do all meetings
            else
                return false;
        }

        return true;
    }
};

// 5
class MinMeetingRoomsRequired
{
    /*
        [1,5] and [5,6] are allowed in one room
        Min heap will act as meeting rooms, the size of min heap after all the meeting will be the answer

        Sort by start time and start allocating meeting rooms to the meeting which start first,
        if any one meeting room is free use it, else use a new meeting room

        T: nlogn(sort) + nlogn(heap) => O(nlogn)
        S:(n) For min heap
    */
    static bool comp(const Interval &a, const Interval &b) { return a.start < b.start; }

public:
    int minMeetingRooms(vector<Interval> &intervals)
    {
        sort(intervals.begin(), intervals.end(), comp);

        // to store end time of each meeting and return the earliest one finishing first
        priority_queue<int, vector<int>, greater<int>> pq_min;

        for (auto interval : intervals)
        {
            // if possible to empty a meeting room do it
            if (!pq_min.empty() && pq_min.top() <= interval.start)
                pq_min.pop();

            // push the current meeting
            pq_min.push(interval.end);
        }
        return pq_min.size();
    }
};

// 6
class MinIntervalForEachQuery
{
    /*
        We will sort intervals by their size and that interval will be the ans for the queries which lie in that interval

        T:O(ilogi + qlogq + ilogq)
        S:O(q(unordered map)+q(result array)+q(set))
    */
    static bool compare_intervals(const vector<int> &a, const vector<int> &b)
    {
        if (a[1] - a[0] == b[1] - b[0])
            return a[0] < b[0]; // if size is same, return the one whose start time is smaller
        return a[1] - a[0] < b[1] - b[0];
    }

public:
    vector<int> minInterval(vector<vector<int>> &intervals, vector<int> &queries)
    {
        vector<int> result(queries.size()); // to store each query ans;
        set<int> s;                         // it will store all queries in sorted order
        unordered_map<int, int> ans;

        for (auto q : queries)
        {
            s.insert(q);
            ans[q] = -1; // set as -1 by default
        }
        // sorted by the smallest size interval first
        sort(intervals.begin(), intervals.end(), compare_intervals);
        // find all queries which are part of intv, set the ans and remove the queries from set
        for (auto intv : intervals)
        {
            if (s.empty())
                break;
            auto it = s.lower_bound(intv[0]);       // O(logq), iterator to first value >= intv[0]
            while (it != s.end() && *it <= intv[1]) // find all queries q, intv[0]<=q<=intv[1]
            {
                ans[*it] = intv[1] - intv[0] + 1;
                it = s.erase(it); // O(1) amortized constant when iterator is used, and returns the next element in order
            }
        }

        int i = 0;
        for (auto q : queries)
            result[i++] = ans[q];

        return result;
    }
};

//
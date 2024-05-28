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
7. Find Median from Data Stream: https://leetcode.com/problems/find-median-from-data-stream/description/
*/

// 7
class MedianFinder
{
    /*
        We will divide the stream into two halfs but we need them in sorted order so we will be using two priority queues,
        1st half will be in pq_max
        2nd half will be in pq_min

        we will maintain pq_max.top() <= pq_min.top()
    */

    priority_queue<int> pq_max;
    priority_queue<int, vector<int>, greater<int>> pq_min;

public:
    MedianFinder() {}

    void addNum(int num)
    {
        // T:O(logn)
        // we will always increase the size of first half i.e pq_max when a number is added
        // to maintain pq_max.top() <= pq_min.top(), we will first insert in 2nd half(pq_min) and from there remove to top element and push in pq_max
        pq_min.push(num);
        pq_max.push(pq_min.top());
        pq_min.pop();

        // if size difference is 2 make both PQs of same size
        if (pq_max.size() - pq_min.size() == 2)
        {
            pq_min.push(pq_max.top());
            pq_max.pop();
        }
    }

    double findMedian()
    {
        // T:O(1)
        // the number of elements are even
        if (pq_max.size() == pq_min.size())
            return (pq_max.top() + pq_min.top()) / 2.0;

        return pq_max.top();
    }
};

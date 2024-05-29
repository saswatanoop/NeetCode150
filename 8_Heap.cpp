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
1. Kth Largest Element in a Stream: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
2. Last Stone Weight: https://leetcode.com/problems/last-stone-weight/description/
3. K Closest Points to Origin: https://leetcode.com/problems/k-closest-points-to-origin/description/
6. Design Twitter: https://leetcode.com/problems/design-twitter/description/
7. Find Median from Data Stream: https://leetcode.com/problems/find-median-from-data-stream/description/
*/

// 1
class KthLargest
{
    /*
        We will use min heap and maintain it's size to be k, so that the Kth largest is at the top of heap
        T:O(logk) S:O(k)
    */
    priority_queue<int, vector<int>, greater<int>> pq_min;
    int size;

    // this will make sure the heap size is never greater than k
    void add_and_maintain_size(const int &val)
    {
        // Each insertion will take O(logk) time
        pq_min.push(val);
        if (pq_min.size() > size)
            pq_min.pop();
    }

public:
    KthLargest(int k, vector<int> &nums)
    {
        size = k;
        for (auto val : nums)
            add_and_maintain_size(val);
    }

    int add(int val)
    {
        add_and_maintain_size(val);
        return pq_min.top();
    }
};

// 2
class LastStone
{
    /*
        We will just simulate the game rules, pick top 2 heaviest and smash them and add it back to remaining stones
        to get top 2 heaviest stones, with multiple insertions while playing thr game we will use max Heap

        T:O(nlogn) S:O(n)
    */
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int> pq_max;
        for (auto s : stones)
            pq_max.push(s);

        while (pq_max.size() > 1)
        {
            auto y = pq_max.top();
            pq_max.pop();
            auto x = pq_max.top();
            pq_max.pop();
            // if the weights are same no need to push to queue as both the stones are destroyed
            if (y != x)
                pq_max.push(y - x); // y will be >= x
        }
        // number of stones remaining can be 0 or 1
        return pq_max.empty() ? 0 : pq_max.top();
    }
};

// 3
class KClosest
{
    /*
        Distance will be ((x-0)^2+(y-0)^2)^0.5, so will just store x^2+y^2 value for distance
        Use max heap of size k so that kth closest will be at the top
        T:O(Nlogk)
        S:O(k)
    */
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        vector<vector<int>> ans;
        priority_queue<pair<int, int>> pq_max;

        // push in max Heap and maintain size k
        for (int i = 0; i < points.size(); i++)
        {
            auto p = points[i];
            // pushing {distance,index}
            pq_max.push({p[0] * p[0] + p[1] * p[1], i});
            if (pq_max.size() > k)
                pq_max.pop();
        }

        // retrieve k closest points using the index
        while (!pq_max.empty())
        {
            ans.push_back(points[pq_max.top().second]);
            pq_max.pop();
        }
        return ans;
    }
};
// 6
class Twitter
{
    /*
        time variable will be used to know which tweet is latest int time;
        S:O(users+tweets)
        T: next to each funtion
    */
    int time;
    unordered_map<int, unordered_set<int>> follows;
    unordered_map<int, vector<pair<int, int>>> tweets; // user->{time,tweets}
public:
    Twitter()
    {
        this->time = 0;
    }

    void postTweet(int userId, int tweetId)
    {
        // T:O(1)
        tweets[userId].push_back({time++, tweetId});
    }

    vector<int> getNewsFeed(int userId)
    {
        /*
            T: users*10*log10=> O(users)
            we will check 10 recent tweets of people user is following, worst case they can follow all users
        */
        vector<int> feed;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq_min;

        // own tweets
        for (int i = tweets[userId].size() - 1, count = 0; i >= 0 && count < 10; i--, count++)
            pq_min.push(tweets[userId][i]);

        // tweets from user they are following, start from end as the latest tweets are inserted at end
        for (auto user_following : follows[userId])
            for (int i = tweets[user_following].size() - 1, count = 0; i >= 0 && count < 10; i--, count++)
            {
                // no need more tweet from this user, since heap already has 10 tweets which are newer than current user
                if (pq_min.size() >= 10 && pq_min.top().first >= tweets[user_following][i].first)
                    break;

                pq_min.push(tweets[user_following][i]);
                if (pq_min.size() > 10)
                    pq_min.pop();
            }

        // retrieve the 10 tweets from heap
        while (!pq_min.empty())
        {
            feed.push_back(pq_min.top().second);
            pq_min.pop();
        }
        // the latest should be first, min priority queue had the least recent of the 10 tweets on top
        reverse(feed.begin(), feed.end());
        return feed;
    }

    void follow(int followerId, int followeeId)
    {
        // T:O(1)
        follows[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId)
    {
        // T:O(1)
        follows[followerId].erase(followeeId);
    }
};

// 7
class MedianFinder
{
    /*
        We will divide the stream into two halfs but we need them in sorted order so we will be using two priority queues,
        1st half will be in pq_max
        2nd half will be in pq_min

        we will maintain pq_max.top() <= pq_min.top()
        S:O(n)
        T: next to each funtion
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

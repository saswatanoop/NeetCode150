
#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <sstream>
#include <climits>
#include <unordered_set>

using namespace std;
/*
1. Sort an Array: https://leetcode.com/problems/sort-an-array/description/
*/
class Sorting
{
    /*
        1. MergeSort => T:O(nlogn) S:O(n)
        2. QuickSort => T:Avg: O(nlogn) Worst: O(n^2) S:O(1)
        3. BucketSort => T:O(n) S:O(n)
     */
    // merge-sort
    void merge(vector<int> &nums, int s, int e)
    {
        vector<int> v(e - s + 1);
        int mid = s + (e - s) / 2;
        int s1 = s;
        int s2 = mid + 1;
        int k = 0;
        while (s1 <= mid || s2 <= e)
        {
            if (s1 > mid || s2 > e)
                v[k++] = s1 <= mid ? nums[s1++] : nums[s2++];
            else
            {
                if (nums[s1] < nums[s2])
                    v[k++] = nums[s1++];
                else
                    v[k++] = nums[s2++];
            }
        }
        k = s;
        for (auto t : v)
            nums[k++] = t;
    }
    void merge_sort(vector<int> &nums, int s, int e)
    {
        // very important, I used s>e and that caused infinite recursion, since s and mid will always remain the same value
        // base case should be 0 or 1 element is always sorted
        if (s >= e)
            return;
        int mid = s + (e - s) / 2;
        merge_sort(nums, s, mid);
        merge_sort(nums, mid + 1, e);
        merge(nums, s, e);
    }
    int generate_random(int s, int e)
    {
        return s + rand() % (e - s + 1);
    }
    // quick-sort
    // same as sort 0s,1s and 2s
    pair<int, int> find_pivot_index(vector<int> &nums, int s, int e, int pivot)
    {
        int i = s, j = e;
        int k = i;

        while (k <= j)
        {
            if (nums[k] == pivot)
                k++;
            else if (nums[k] < pivot)
            {
                swap(nums[i], nums[k]);
                i++;
                k++;
            }
            else
            {
                swap(nums[j], nums[k]);
                j--;
            }
        }
        return {i, j};
    }
    void quick_sort(vector<int> &nums, int s, int e)
    {
        if (s >= e)
            return;

        int pivot = nums[generate_random(s, e)];
        auto pivot_index = find_pivot_index(nums, s, e, pivot);
        quick_sort(nums, s, pivot_index.first - 1);
        quick_sort(nums, pivot_index.second + 1, e);
    }

public:
    vector<int> sortArray(vector<int> &nums)
    {
        srand(time(0));
        quick_sort(nums, 0, nums.size() - 1);
        return nums;
    }
};
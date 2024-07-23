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

// PQ comparator
class CompareForPQ
{
public:
    // max heap using b.first and b.second values
    bool operator()(const pair<int, int> &a, const pair<int, int> &b)
    {
        if (a.first == b.first)
            return a.second < b.second;
        return a.first < b.first;
    }
};
// Sort comparator
bool compare_for_sort(const int &a, const int &b)
{
    // Sort in decreasing order, a decides the order here
    return a > b;
}

// Splitting sentences into words
#include <sstream>
class HowToSplitString
{
public:
    void learn_stringstream()
    {
        string str = "apple,banana,orange,grape";
        stringstream steam(str);
        string item;
        vector<string> tokens;

        while (getline(steam, item, ','))
        {
            tokens.push_back(item);
        }
    }
};

int main()
{
    priority_queue<pair<int, int>, vector<pair<int, int>>, CompareForPQ> pq_max;
    vector<int> vec = {1, 5, 3, 4, 2};
    sort(vec.begin(), vec.end(), compare_for_sort);
}
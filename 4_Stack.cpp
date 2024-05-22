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
1. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/description/
2.
*/

class ValidParantheses
{
public:
    bool isValid(string s)
    {
        stack<char> st;

        unordered_map<char, char> um = {{'(', ')'}, {'{', '}'}, {'[', ']'}};
        for (auto c : s)
        {
            if (c == '(' || c == '{' || c == '[')
                st.push(c);
            else
            {
                if (st.empty() || um[st.top()] != c)
                    return false;
                // This below point don't miss
                else
                    st.pop();
            }
        }
        // don't miss below point if stack is empty or not
        return st.empty();
    }
};
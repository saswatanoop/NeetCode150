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
2. Min Stack: https://leetcode.com/problems/min-stack/description/
3. Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
*/

// 1.
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

// 2.
class MinStackUsingOneStack
{
    stack<pair<int, int>> s;

public:
    MinStackUsingOneStack()
    {
    }

    void push(int val)
    {
        int minVal = s.empty() ? val : min(s.top().second, val);
        s.push({val, minVal});
    }

    void pop()
    {
        s.pop();
    }

    int top()
    {
        return s.top().first;
    }

    int getMin()
    {
        return s.top().second;
    }
};
class MinStackUsingTwoStacks
{
public:
    stack<int> s;  // normal stack
    stack<int> ms; // min stack
    MinStackUsingTwoStacks()
    {
    }

    void push(int val)
    {
        s.push(val);
        // if the item pushed is less than or equal to the min till now push it
        if (ms.empty() || val <= ms.top())
            ms.push(val);
    }

    void pop()
    {
        // pop from min top if the stack top is same as min-top
        if (s.top() == ms.top())
            ms.pop();
        s.pop();
    }

    int top()
    {
        return s.top();
    }

    int getMin()
    {
        return ms.top();
    }
};

class EvalRPN
{
    /*
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

    */
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> st;
        unordered_set<string> operations = {"+", "-", "/", "*"};
        for (auto token : tokens)
        {
            if (operations.find(token) == operations.end())
                st.push(stoi(token));
            else
            {
                int right = st.top();
                st.pop();
                int left = st.top();
                st.pop();
                int ans;
                if (token == "+")
                    ans = left + right;
                else if (token == "-")
                    ans = left - right;
                else if (token == "*")
                    ans = left * right;
                else if (token == "/")
                    ans = left / right;
                st.push(ans);
            }
        }
        return st.top();
    }
};
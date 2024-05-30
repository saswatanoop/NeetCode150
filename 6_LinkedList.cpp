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
1. Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/description/
*/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class ReverseLinkList
{
    /*
        1. Iterative:
            T:O(n) S:O(1)
        2. Recursive:
            T:O(n) S:O(n) space of stack
    */
public:
    ListNode *reverseListItr(ListNode *head)
    {
        // we will use 3 pointers prev, cur, next and keep setting cur->next =prev and use next to move the cur

        ListNode *prev = NULL;
        while (head)
        {
            ListNode *next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
    ListNode *reverseList(ListNode *head)
    {
        // Base case
        if (!head || !head->next)
            return head;

        // 1->2->3->4->5
        ListNode *root = reverseList(head->next);
        // we have 1->2 and 5->4->3->2 we will use 1->2->next to set 2->1 and set 1->NULL, resulting in 5->4->3->2->1
        head->next->next = head;
        head->next = NULL;
        return root;
    }
};
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
2. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/description/
*/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 1
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

// 2
class MergeTwoSortedList
{
    /*
        Same way we do merge in merge sort
            T:O(n) S:O(1)
    */
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        // we will use ans.next to store the start of merge list
        ListNode ans;
        ListNode *temp = &ans;

        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                temp->next = list1;
                list1 = list1->next;
            }
            else
            {
                temp->next = list2;
                list2 = list2->next;
            }
            temp = temp->next;
        }
        // attach the remaining list whichever is remaining
        if (list1)
            temp->next = list1;

        if (list2)
            temp->next = list2;

        return ans.next;
    }
};

//
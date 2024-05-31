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
3. Reorder List: https://leetcode.com/problems/reorder-list/description/
6. Add Two Numbers: https://leetcode.com/problems/add-two-numbers/description/
7. Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/
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

// 3
class ReorderList
{
    /*
        T:O(n) S:O(1)
        1. break into two halfs
        2. reverse second half
        3. merge both the lists first_half and second_half
    */
    ListNode *reverseLL(ListNode *head)
    {

        ListNode *prev = NULL;
        while (head)
        {
            auto next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }

public:
    void reorderList(ListNode *head)
    {
        if (!head || !head->next)
            return;

        // break into two halfs, by getting the mid, consider both the cases even and odd length list
        auto slow = head, fast = head;
        while (fast && fast->next && fast->next->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        auto first_half = head;
        auto second_half = slow->next;
        slow->next = NULL;

        // reverse second half
        second_half = reverseLL(second_half);

        // merge both the lists first_half and second_half
        ListNode ans;
        auto temp = &ans;
        bool use_first_half = true;

        while (first_half || second_half) // OR used here as elements in first half >= elements in second half
        {
            if (use_first_half)
            {
                temp->next = first_half;
                first_half = first_half->next;
            }
            else
            {
                temp->next = second_half;
                second_half = second_half->next;
            }
            // change the half to use
            use_first_half = !use_first_half;
            temp = temp->next;
        }
    }
};

// 6
class AddTwoNumbers
{
    /*
        Here the number is alredy given in reverse, if not we will need to do below extra steps
            1. we need to reverse both lists
            2. Add both lists
            3. Return reverse of both lists

    */
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode ans;
        ListNode *temp = &ans;

        int carry = 0;
        while (l1 || l2 || carry)
        {
            int a = l1 ? l1->val : 0;
            int b = l2 ? l2->val : 0;
            int sum = a + b + carry;
            carry = sum / 10;
            temp->next = new ListNode(sum % 10);
            temp = temp->next;

            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
        }
        return ans.next;
    }
};

// 7
class CheckCycle
{
public:
    bool hasCycle(ListNode *head)
    {
        auto slow = head, fast = head;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
                return true;
        }
        return false;
    }
};
//
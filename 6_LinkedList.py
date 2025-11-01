from typing import Optional, List
from collections import defaultdict, OrderedDict
import heapq


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. https://leetcode.com/problems/reverse-linked-list/
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # keep three pointes, prev, head and next
    # T:O(n) S:O(1)
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


# 2. https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    # T:O(n) and S:O(1)

    dummy = ListNode()
    temp = dummy
    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    # if anyone of the list is remaining directly append it
    temp.next = list1 or list2

    return dummy.next


# 3. https://leetcode.com/problems/linked-list-cycle/
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # T:O(n) and S:O(1)

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# 4. https://leetcode.com/problems/reorder-list/
def reorderList(self, head: Optional[ListNode]) -> None:
    # T:O(n) and S:O(1)
    # 1. find middle
    # 2. reverse the second half
    # 3. merge both first and reversed second half
    def merge_lists(
        l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        use_first = True
        while l1 or l2:
            if use_first:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            use_first = not use_first
        return dummy.next

    def reverse_list(l: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while l:
            next = l.next
            l.next = prev
            prev = l
            l = next
        return prev

    if not head or not head.next:
        return

    # we need to stop at one place before second half
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    l2 = slow.next  # second half
    slow.next = None  # break the list in 2 halfs
    l1 = head
    l2 = reverse_list(l2)
    head = merge_lists(l1, l2)


# 5. https://leetcode.com/problems/remove-nth-node-from-end-of-list/
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # T:O(n) and S:O(1)
    # Adding dummy will help remove the nth node, that is the head node itself easily
    dummy = ListNode()
    dummy.next = head
    prev_to_delete = fast = dummy
    while n and fast.next:
        fast = fast.next
        n -= 1
    # the n provided is higher than list size
    if n != 0:
        return False
    while fast.next:
        fast = fast.next
        prev_to_delete = prev_to_delete.next

    prev_to_delete.next = prev_to_delete.next.next
    return dummy.next


# 6. https://leetcode.com/problems/copy-list-with-random-pointer/
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # T:O(3*n) S:O(1)
        if not head:
            return None
        # 1st iteration: create a copy adjacent to the orignial node
        l1 = head
        while l1:
            copy = Node(l1.val)
            copy.next = l1.next  # remember what was next to l1 first and add copy->l2
            l1.next = copy  # l1->copy, so it becomes l1->copy->l2
            l1 = copy.next  # Move l1 to next element after copy

        # 2nd iteration: match the random pointers
        l1 = head
        while l1:
            copy = l1.next
            # Mistake: missed the if condition
            if l1.random:
                copy.random = l1.random.next
            l1 = copy.next

        # 3rd Iteration: separate into 2 lists, orignal and copy
        l1 = head
        l2 = head.next  # l2 has the head of copied linked list
        while l1:
            copy = l1.next
            l1.next = copy.next
            l1 = l1.next
            # Mistake: missed the if condition
            if l1:
                copy.next = l1.next
        return l2

    def copyRandomList_one_pass_n_space(
        self, head: "Optional[Node]"
    ) -> "Optional[Node]":
        # T:O(n) S:O(n)
        dic = defaultdict(Node)
        temp = head
        while temp:
            if temp not in dic:
                dic[temp] = Node(temp.val)
            if temp.next:
                if temp.next not in dic:
                    dic[temp.next] = Node(temp.next.val)
                dic[temp].next = dic[temp.next]
            if temp.random:
                if temp.random not in dic:
                    dic[temp.random] = Node(temp.random.val)
                dic[temp].random = dic[temp.random]
            temp = temp.next

        return dic[head] if head else None


# 7. https://leetcode.com/problems/add-two-numbers/
def addTwoNumbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    # T:O(n) S:O(1)
    dummy = ListNode()
    temp = dummy
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        temp.next = ListNode(carry % 10)
        temp = temp.next
        carry = carry // 10

    return dummy.next


# 8. https://leetcode.com/problems/find-the-duplicate-number/
def findDuplicate(self, nums: List[int]) -> int:
    # T:O(n) and S:O(1)
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


# 9. https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        # most recent one will be at the start and oldest willl be at the end
        self.ordered_dic = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # T:O(1) and S:O(capacity)
        if key not in self.ordered_dic:
            return -1
        # move key to front
        self.ordered_dic.move_to_end(key, last=False)
        return self.ordered_dic[key]

    def put(self, key: int, value: int) -> None:
        # T:O(1) and S:O(capacity)
        # if capacity reached and we need to insert new element remove from the end
        if key not in self.ordered_dic and len(self.ordered_dic) == self.capacity:
            self.ordered_dic.popitem(last=True)
        self.ordered_dic[key] = value
        # move key to front
        self.ordered_dic.move_to_end(key, last=False)


# 10. https://leetcode.com/problems/merge-k-sorted-lists/description/
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # T:O(nlogk) and S:O(k)
    dummy = ListNode()
    min_heap = []
    temp = dummy
    counter = 0
    for l in lists:
        if l:
            heapq.heappush(min_heap, (l.val, counter, l))
            counter += 1

    while min_heap:
        l = heapq.heappop(min_heap)[2]
        temp.next = l
        l = l.next
        if l:
            heapq.heappush(min_heap, (l.val, counter, l))
            counter += 1
        temp = temp.next

    return dummy.next


# 11. https://leetcode.com/problems/reverse-nodes-in-k-group/
class Solution:
    def reverseLL(self, node):
        last = node
        prev = None
        while node:
            cur = node
            node = node.next
            cur.next = prev
            prev = cur
        return prev, last

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # T:O(n) and S:O(1)
        if k == 1 or not head:
            return head
        dummy = ListNode()
        temp = dummy
        rem = head

        while rem:
            n = k - 1  # since we are already at first node, it is already counted
            group_start = rem
            while rem and n:
                rem = rem.next
                n -= 1
            if rem:  # do the reversal
                group_last = rem
                rem = rem.next
                group_last.next = None
                group_head, group_tail = self.reverseLL(group_start)
                temp.next = group_head
                temp = group_tail
            else:  # not enough size to reverse, just add to list
                temp.next = group_start

        return dummy.next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. https://leetcode.com/problems/reverse-linked-list/
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # keep three pointes, prev, head and next
    # T:O(n) S:O(1)
    prev=None
    while head:
        next=head.next
        head.next=prev
        prev=head
        head=next
    
    return prev

# 2. https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # T:O(n) and S:O(1)
    
    dummy=ListNode()
    temp=dummy    
    while list1 and list2:
        if list1.val<list2.val:
            temp.next=list1
            list1=list1.next
        else:
            temp.next=list2
            list2=list2.next
        temp=temp.next
    
    # if anyone of the list is remaining directly append it
    temp.next = list1 or list2
    
    return dummy.next

# 3. https://leetcode.com/problems/linked-list-cycle/
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # T:O(n) and S:O(1)
   
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    
    return False

# 4. https://leetcode.com/problems/reorder-list/
def reorderList(self, head: Optional[ListNode]) -> None:
    # T:O(n) and S:O(1)
    # 1. find middle
    # 2. reverse the second half
    # 3. merge both first and reversed second half
    def merge_lists(l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
        dummy =ListNode()
        temp=dummy
        use_first=True
        while l1 or l2:
            if use_first:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
            use_first=not use_first
        return dummy.next
    
    def reverse_list(l:Optional[ListNode])->Optional[ListNode]:
        prev=None
        while l:
            next=l.next
            l.next=prev
            prev=l
            l=next
        return prev

    if not head or not head.next:
        return

    # we need to stop at one place before second half
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    l2=slow.next #second half
    slow.next=None # break the list in 2 halfs
    l1=head 
    l2=reverse_list(l2)
    head=merge_lists(l1,l2)
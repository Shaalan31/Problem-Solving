# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr1 = head
        ptr2 = head
        while(ptr2.next is not None):
            ptr2 = ptr2.next
            ptr1= ptr1.next
            if(ptr2.next is not None):
                ptr2 = ptr2.next
        return ptr1
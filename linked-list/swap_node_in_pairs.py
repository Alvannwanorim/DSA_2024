# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        cur = head
        prev = dummy
        while cur and cur.next:
            nextPtr = cur.next.next
            second = cur.next
            
            second.next = cur
            cur.next = nextPtr
            prev.next = second

            prev = cur
            cur = nextPtr
        return dummy.next

        

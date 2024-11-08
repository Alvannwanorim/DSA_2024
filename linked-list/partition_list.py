# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)
        iLeft, iRight = left, right
        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next
        
        left.next = iRight.next
        right.next = None
    
        return iLeft.next
        

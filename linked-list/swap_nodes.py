# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur = head
        for i in range(1, k):
            cur = cur.next
        left = cur
        right = head 
        while cur.next:
            right = right.next
            cur = cur.next
        print(right.val, )
        left.val, right.val = right.val, left.val

        return head

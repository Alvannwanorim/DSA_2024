# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
        
        dummy= ListNode()
        cur = dummy
        for n in stack:
            node = ListNode(n)
            cur.next = node
            cur = node
        return dummy.next

        
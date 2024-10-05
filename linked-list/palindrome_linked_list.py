# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        cur = head 
        table = []
        while cur:
            table.append(cur.val)
            cur = cur.next
        l = 0
        r = len(table) -1 
        while l < r:
            if table[l] != table[r]:
                return False
            l += 1
            r -= 1
        return True
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        # 2 <- 3 <- 4 <- 5
        while slow:
            node = ListNode(slow.val)
            node.next = prev
            prev = node
            slow = slow.next
        
        start = head
        end = prev
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True        
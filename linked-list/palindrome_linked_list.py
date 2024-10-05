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
        
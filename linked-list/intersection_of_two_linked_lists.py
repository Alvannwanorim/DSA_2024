# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = headA, headB
        while listA != listB:
            listA = listA.next if listA else headA
            listB = listB.next if listB else headB
        return listA
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        l = 0
        ptr1 = None
        while l < a:
            ptr1= cur
            cur = cur.next
            l += 1
        ptr1.next = list2
        
        while l < b + 1:
            cur = cur.next
            l += 1
        print(cur.val)

        cur2 = list2
        while cur2.next:
            cur2 = cur2.next
        cur2.next = cur

        print(cur2.val, cur.val)
        return list1
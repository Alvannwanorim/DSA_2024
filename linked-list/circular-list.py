from typing import List


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class CircularList:
    #constructor
    def __init__(self, head:Node|None=None) -> None:
        self.head = None
    
    def create(self,nums:List[int]):
        node = Node(nums[0])
        
        self.head = node
        curr = self.head
        for i in range(1,len(nums)):
            new_node = Node(nums[i])
            curr.next = new_node
            curr = curr.next
        curr.next = self.head

    def isCircular(self):
        slowPtr = self.head
        fastPtr = self.head
        fastPtr = fastPtr.next
        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            try:
                fastPtr = fastPtr.next.next
            except ValueError:
                return False
        return True
    def printList(self):
        curr = self.head
        res = []
        count = 1
        while curr !=  None:
            # print(curr.data)
            if count > 5:
                return res
            count += 1
            res.append(curr.data)
            curr = curr.next
        return res
list1 = CircularList()
list1.create([1,2,3,4,5])
print(list1.isCircular())


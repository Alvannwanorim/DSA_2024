from typing import List


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    #constructor
    def __init__(self, head:Node|None=None) -> None:
        self.head = None
        self.length = 0
    
    def insertMany(self,nums:List[int]):
        node = Node(nums[0])
        
        self.head = node
        curr = self.head
        for i in range(1,len(nums)):
            new_node = Node(nums[i])
            curr.next = new_node
            curr = curr.next
            self.length += 1
    
    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.next
        return res
    
    def reverse(self):
        curr = self.head
        # print(curr, curr.data)
        prev = None
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        self.head = prev
list1 = LinkedList()
list1.insertMany([1,2,3,4,5])
list1.reverse()
print(list1.printList())

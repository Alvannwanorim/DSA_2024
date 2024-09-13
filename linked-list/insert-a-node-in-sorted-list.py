from typing import List


class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.next = None

class LinkedList:
    #constructor
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    def insertMany(self,nums:List[int]):
        print(nums[0])
        node = Node(nums[0])
        
        self.head = node
        curr = self.head
        for i in range(1,len(nums)):
            new_node = Node(nums[i])
            curr.next = new_node
            curr = curr.next

    def insertNode(self,data: int):
        node = Node(data)
        if self.head is None or self.head.data > data:
            node.next = self.head
            self.head = node
            return
        cur = self.head
        while cur.next is not None and cur.next.data < data:
                cur = cur.next
        
        node.next = cur.next
        cur.next = node
       
    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.next
        print(res)

list1 = LinkedList()
list1.insertMany([1,2,3,4,5])
list1.insertNode(6)
list1.insertNode(0)
list1.insertNode(2)
list1.printList()
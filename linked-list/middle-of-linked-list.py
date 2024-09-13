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

    def middle(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        middleNode = count //2 

        count = 0 
        curr = self.head
        while count < middleNode:
            curr = curr.next
            count += 1
        print(curr.data)
        
    def middle2(self):
        slowPtr = self.head
        fastPtr = self.head
        count = 0
        while fastPtr:
            fastPtr = fastPtr.next
            if fastPtr is None:
                print(slowPtr.data)
                return
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        print(slowPtr.data)
        

       
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
list1.middle()
list1.middle2()
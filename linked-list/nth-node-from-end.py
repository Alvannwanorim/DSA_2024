from typing import List


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next

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

    def nthNodeFromEnd2(self, n):
        curr = self.head
        curr2 = self.head
        count = 0
        while count < n:
            # print(count)
            count += 1
            curr = curr.next

        while curr:
            curr2 = curr2.next
            curr = curr.next
        return curr2.data
    
    def nthNodeFromEnd(self, n):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        print(count)
        
        nthNode = count - n + 1

        curr = self.head
        count = 1
        while curr:
            if count == nthNode:
                return curr.data
            curr = curr.next
            count += 1

    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.next
        return res
    
list1 = LinkedList()
list1.insertMany([3,6,2,4,5])
print(list1.nthNodeFromEnd(3))
print(list1.nthNodeFromEnd2(3))

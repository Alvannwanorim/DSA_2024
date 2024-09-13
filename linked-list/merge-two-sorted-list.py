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
        node = Node(nums[0])
        
        self.head = node
        curr = self.head
        for i in range(1,len(nums)):
            new_node = Node(nums[i])
            curr.next = new_node
            curr = curr.next
    
    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.next
        print(res)

def mergeList(l1:LinkedList, l2:LinkedList):
    dummy = Node(0)
    ptr1 = l1.head
    ptr2 = l2.head
    prev = dummy
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data < ptr2.data:
            prev.next = ptr1
            prev = prev.next
            ptr1 = ptr1.next
        else:
            prev.next= ptr2
            prev = prev.next
            ptr1 = ptr2.next
    if ptr1 is not None:
        prev.next = ptr1
    if ptr2 is not None:
        prev.next = ptr1
    return dummy.next

list1 = LinkedList()
list2 = LinkedList()
list1.insertMany([1,3,5])
list2.insertMany([2,4,6])

list3 = mergeList(list1,list2)
print(list3)


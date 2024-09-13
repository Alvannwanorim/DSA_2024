
from typing import List


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    # Get the next node
    def getNext(self):
        return self.next

    # set the pointer of the node to a new node
    def setNext(self,next):
        self.next = next

    def setPrev(self,prev):
        self.prev = prev

    def getPrev(self):
        return self.prev
     
    def  getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def hasNext(self):
        return self.next != None

class DoublyLinkedList:
    def __init__(self,head: Node| None=None) -> None:
        self.head = head
        self.length = 0

    def append(self, data):
        node = Node()
        node.setData(data)
        if self.head is None:
            self.head = node
            self.length += 1
            return
        
        curr = self.head
        while curr.getNext() != None:
            curr = curr.getNext()
        curr.setNext(node)
        node.setPrev(curr)
        self.length += 1
    
    def unshift(self,data):
        node = Node()
        node.setData(data)

        if self.head is None:
            self.head =node
            self.length += 1

        self.head.setPrev(node)
        node.setNext(self.head.next)
        node.setPrev(self.head)
        self.head = node
        # cur = None
        self.length += 1

    def insertAt(self, data, pos):
        if pos > self.length:
            return
        if pos == 0:
            return self.unshift(data) 
        if pos == self.length:
            return self.append(data)
        
        node = Node()
        node.setData(data)
        curr = self.head
        prev = None
        count = 0
        while count < pos - 1:
            count += 1
            prev = curr
            curr = curr.getNext()

        node.setNext(curr)
        node.setPrev(prev)
        curr.setPrev(node)
        prev.setNext(node)
        self.length += 1

    def insertMany(self, nums: List[int]):
        for n in nums:
            self.append(n)

    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.getNext()
        return res
    

linkedList = DoublyLinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.insertAt(2,3)
# linkedList.insertMany([1,2,3,4,5])
# linkedList.pop()
# linkedList.deleteAt(1)
# linkedList.deleteAt(2)
# linkedList.deleteAt(3)
print(linkedList.printList())
        
    

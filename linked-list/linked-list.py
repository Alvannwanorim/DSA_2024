from typing import List


class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    
    # Get the next node
    def getNext(self):
        return self.next
    # get the node data 
    def  getData(self):
        return self.data
    # set the pointer of the node to a new node
    def setNext(self,next):
        self.next = next
    
    def setData(self, data):
        self.data = data

    def hasNext(self):
        return self.next != None

class LinkedList:
    #constructor
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def append(self,data):
        curr_node = Node()
        curr_node.setData(data)
        if self.head  is None:
            self.head = curr_node
            return
        last_node = self.head
        while last_node.getNext() != None:
            last_node= last_node.getNext()
        last_node.setNext(curr_node)
        self.length += 1
    def pop(self):
        if self.head is None:
            return
        cur = self.head
        last_node = Node
        while cur.getNext() !=  None:
            last_node = cur
            cur = cur.getNext()
        last_node.next = None
        cur= None
        self.length -= 1
        
    def deleteAt(self,pos):
        if pos < 0 or pos > self.length:
            return
        if self.head is None:
            return
        if pos == 0:
            self.unshift()
            return
        if pos == self.length:
            self.pop()
            return
        count = 0
        curr = self.head
        while count < pos - 1:
            curr = curr.getNext()
            count += 1
        node = curr.getNext()
        curr.setNext(node.getNext())
        self.length  -= 1
    def unshift(self):
        if self.head is None:
            return
        self.head = self.head.getNext()
        self.length -= 1
    def deleteNodeWithKey(self, key):
        # return if the linked list is empty 
        if self.head  is None:
            return
        curr = self.head
        # check if the key is at the head
        if curr and curr.getData() == key:
            self.head = curr.getNext()
            curr = None
            self.length -= 1
            return
        prev = None
        #Loop through the list to find the key
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # if there is no key found
        if curr is None:
            return 
        #change the pointer 
        prev = curr.next
        # reduce the length of the node
        self.length -= 1
        # delete the node 
        curr = None
    def printList(self):
        curr = self.head
        res = []
        while curr !=  None:
            # print(curr.data)
            res.append(curr.data)
            curr = curr.getNext()
        return res
    def inserAtPosition(self,pos, data):
        if self.length < pos:
            return
        if pos == 0 or pos == self.length:
            self.append(data)
            return
        count = 0
        curr = self.head
        while count < pos -1:
            count += 1
            curr = curr.getNext()
        node = Node()
        node.setData(data)
        node.setNext(curr.getNext)
        curr.setNext(node)
        self.length +=1 

    def insertMany(self, nums: List[int]):
        for n in nums:
            self.append(n)
        

linkedList = LinkedList()
linkedList.insertMany([1,2,3,4,5])
# linkedList.pop()
linkedList.deleteAt(1)
linkedList.deleteAt(2)
linkedList.deleteAt(3)
print(linkedList.printList())
        
    

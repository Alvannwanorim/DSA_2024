class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head= None
        self.size = 0

    def get(self, index: int) -> int:
        if not self.head or index < 0 or index >= self.size:
            return -1
        cur = self.head
        while cur and index > 0:
            cur = cur.next
            index -= 1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.size +=1 
            return
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head= node
            self.size += 1
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        node = ListNode(val)
        cur = self.head
        count = 0
        while count < index - 1:
            cur = cur.next
            count += 1
        nxt = cur.next
        cur.next = node
        node.next = nxt
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or not self.head:
            return 
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur = self.head
        while cur and index > 1:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
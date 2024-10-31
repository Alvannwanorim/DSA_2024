class ListNode:
    def __init__(self,key):
        self.next = None
        self.key = key 

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        indx = key % len(self.set)
        cur = self.set[indx]

        while cur.next:
            if cur.next.key == key:
                return key
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        indx = key % len(self.set)
        cur = self.set[indx]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next

        return 

    def contains(self, key: int) -> bool:
        indx = key % len(self.set)
        cur = self.set[indx].next

        while cur:
            if cur.key == key:
                print(cur.key)
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
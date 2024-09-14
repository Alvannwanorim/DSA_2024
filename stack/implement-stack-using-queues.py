from collections import deque


class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.q)- 1):
            self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.q)- 1):
            self.push(self.q.popleft())
        res =  self.q.popleft()
        self.push(res)
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0

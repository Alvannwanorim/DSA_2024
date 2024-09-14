class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1],val))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        
        
sol = MinStack()
sol.push(1)
sol.push(2)
sol.push(0)
print(sol.getMin())
print(sol.pop())
print(sol.top())
print(sol.getMin())

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

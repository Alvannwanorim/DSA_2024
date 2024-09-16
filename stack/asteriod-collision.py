class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for n in asteroids:
            while stack and n < 0 and stack[-1] > 0:
                diff = n + stack[-1]
                if diff > 0:
                    n = 0
                elif diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    n = 0
                else:
                    stack.pop()
            if n:
                stack.append(n)
        return stack
            
            
        return stack
        
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for s in operations:
            if s == '+':
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif s == 'D':
                double_value = stack[-1] * 2
                stack.append(double_value)
            elif s == 'C':
                stack.pop()
            else:
                stack.append(int(s))
        return sum(stack)

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(["1","C"]))
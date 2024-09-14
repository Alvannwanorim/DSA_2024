class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) != len(popped):return False

        i = 0
        stack = []

        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
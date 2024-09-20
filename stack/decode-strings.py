class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                cur = ''
                num = ''
                while stack and stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                cur = cur * int(num)
                stack.append(cur)
                cur =''
            else:
                stack.append(s[i])
        return "".join(stack)
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))
print(sol.decodeString("100[leetcode]"))
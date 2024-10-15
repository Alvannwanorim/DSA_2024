class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split(" ")
        res = []
        for c in stack:
            res.append(c[::-1])
        return " ".join(res)
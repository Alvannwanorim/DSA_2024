from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.is_palindrome(w):
                return w
        return ""
    def is_palindrome(self,w):
        l = 0
        r = len(w) - 1
        while l < r:
            if w[l] != w[r]:
                return False
            l += 1
            r -= 1
        return True

        
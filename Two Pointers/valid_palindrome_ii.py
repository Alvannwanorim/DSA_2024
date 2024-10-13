class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1:r +1]
                skipR = s[l:r]
                print(skipL,skipR)
                return (skipL == skipL[::-1] or skipR== skipR[::-1])
            l += 1
            r -= 1
        return True

class Solution2:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1:r +1]
                skipR = s[l:r]
                return (self.isPalindrome(skipL) or self.isPalindrome(skipR))
            l += 1
            r -= 1
        return True
    def isPalindrome(self, s: str):
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
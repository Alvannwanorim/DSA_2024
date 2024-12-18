class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len=0 
        res =''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > res_len:
                    res_len= length
                    res= s[l: r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r <len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > res_len:
                    res_len= length
                    res= s[l: r + 1]
                l -= 1
                r += 1
        return res 
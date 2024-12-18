class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            count.add(s[r])
        return res
            
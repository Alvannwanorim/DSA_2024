from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            if dp[i] == True:
                for w in wordDict:
                    if(s[i: i + len(w)] == w and i + len(w)<= n):
                        dp[i + len(w)] = True
        return dp[n]
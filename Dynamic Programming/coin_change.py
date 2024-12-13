from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(a):
            if a in memo:
                return memo[a]
            if a == 0:
                return 0
            
            res = 1e9
            for c in coins:
                if a - c >= 0:
                    res = min (res, 1 + dfs(a - c))
            memo[a] = res
            return res 
        res = dfs(amount)
        return res if res < 1e9 else -1
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount +1 else -1

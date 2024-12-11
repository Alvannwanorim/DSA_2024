class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1]= 1
        dp[2] = 2
        
        for i in range(3,n + 1):
            dp[i]= dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]

class Solution2:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one + two
            two = one
            one = temp
        return one
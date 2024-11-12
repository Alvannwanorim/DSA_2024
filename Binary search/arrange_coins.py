class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        res = 0
        while l <= r:
            m = (r + l) // 2
            coins = (m/2) * (m + 1)
            if coins > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        
        return res

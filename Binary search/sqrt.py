class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while l <= r:
            m = l + ( r - r)  

            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                res = m 
                l = m + 1
            else:
                return m
        
        return res
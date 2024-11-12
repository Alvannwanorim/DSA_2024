from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for n in nums:
            xor ^= n
        
        diff_bit = 1

        while not (xor & diff_bit):
            diff_bit = diff_bit << 1

        print(diff_bit)
        a, b = 0, 0
        for n in nums:
            if diff_bit & n:
                a = a ^ n
            else:
                b= b ^ n
        
        return [a,b]
    
sol =Solution()
print(sol.singleNumber([1,2,1,3,2,5]))
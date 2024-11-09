from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0 
        sub_sum = sum(arr[: k])
        min_sum = threshold * k 
        if sub_sum >= min_sum:
            res += 1
        for r in range(k, len(arr)):
            sub_sum += arr[r] - arr[l]
            l +=1 
            if sub_sum >= min_sum:
                res += 1
        return res
            


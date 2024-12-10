from typing import List


def bestSum(target:int, nums: List[int]):
    dp= [None] * (target + 1)
    dp[0] = []
    for i in range(target + 1):
        if dp[i] != None:
            for n in nums:
                if i + n <= target:
                    comb = dp[i] + [n]
                    if dp[i + n] is None or len(dp[i + n]) > len(comb):
                        dp[i + n] = comb
    return dp[target]

print(bestSum(7, [2,3]))
print(bestSum(7, [5,4,3,7]))
print(bestSum(7, [2,4]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))
print(bestSum(100, [25,1,2,5]))
from typing import List


def howSum(target:int, nums: List[int]):
    dp = [None] * (target + 1)
    dp[0] = []
    for i in range(target + 1):
        if(dp[i] != None):
            for n in nums:
                if(i + n) <= target:
                    dp[i + n] = dp[i] + [n]
    # print(dp)
    return dp[target]
print(howSum(7, [2,3]))
print(howSum(7, [5,4,3,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7, 14]))

from typing import List


def targetSum(target: int, nums:List[int]):
    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(target + 1):
        if dp[i] == True:
            for n in nums:
                if i + n <= target:
                    dp[i + n] = True
    print(dp)
    return dp[target]

print(targetSum(2,[3,4,5]))
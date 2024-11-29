def maxContiguousSum(nums):
    maxSum = 0
    n= len(nums)
    for i in range(1,n):
        for j in range(i, n):
            curSum  = 0
            for k in range(i, j + 1):
                curSum += nums[k]
                if curSum > maxSum:
                    maxSum = curSum
    return maxSum

def maxContiguousSum2(nums):
    maxSum = 0
    n = len(nums)
    for i in range(1,n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            maxSum = max(curSum, maxSum)
    return maxSum

def maxContiguousSumDp(nums):
    maxSum = 0
    n = len(nums)
    dp = [0] * (n + 1)

    if(nums[0] > 0):
        dp[0] = nums[0]
    
    for i in range(1, n):
        if(dp[i - 1] + nums[i] > 0):
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = 0
    print(dp)
    for i in range(n):
        maxSum = max(maxSum, dp[i])

    return maxSum

print(maxContiguousSumDp([-2,3,-16,100,-4,5]))
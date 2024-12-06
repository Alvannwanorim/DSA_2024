def travelGrid(m,n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            curr = dp[i][j]
            if j + 1 <= n:
                dp[i][j + 1] += curr
            if i + 1<= m:
                dp[i + 1][j] += curr
    # print(dp)
    return dp[m][n]
print(travelGrid(1,1))
print(travelGrid(2,3))
print(travelGrid(3,2))
print(travelGrid(3,3))
print(travelGrid(6,6))
print(travelGrid(18,18))
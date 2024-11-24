def fib(n):
    dp = [0,1 ]
    for i in range(2, n+1):
        dp.append(dp[i - 1] + dp[i -2])
    return dp[n]

# print(fib(10))

def fib2(n):
    fibTable = {1:1,2:1}
    def calc(n):
        if n <= 2:
            return 1
        if n in fibTable:
            return fibTable[n]
        else:
            fibTable[n] = calc(n -1 ) + calc(n - 2)
            return fibTable[n]
    return calc(n)

print(fib2(5))
print(fib2(10))
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

def fib3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
print(fib3(5))
print(fib3(10))
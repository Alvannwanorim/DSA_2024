"""
Calculates the fibonaci series

"""
def fibonaci(n: int, memo={}):
    # check for the base case
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    # returns the sum of the fibonaci numbers
    memo[n] = fibonaci( n - 1 ) + fibonaci(n - 2)

    return memo[n]


print(fibonaci(1))
print(fibonaci(2))
print(fibonaci(5))
print(fibonaci(8))
print(fibonaci(20))
print(fibonaci(50))

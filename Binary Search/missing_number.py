def missingNumber(num):
    n = len(num)
    X = 0
    for i in range(1,n + 2):
        x = X ^ i
    print(X)
    for i in range(0,n):
        X = X^num[i]
    return X

print(missingNumber([1,2,3,4,5,7]))
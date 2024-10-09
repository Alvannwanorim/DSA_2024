def oddOccurence(num):
    # X = num[0]
    # for i in range(1,len(num)):
    #     X = X ^ num[i]
    X = 0
    for n in num:
        X = X ^ n

    return X 

print(oddOccurence([2,2,3,3,3,4,4,5,5,6,6]))
print(oddOccurence([1,2,3,1,2,3,1]))
def dutchFlagProblem(nums):
    c0 = 0
    c1 = 0
    c2 = 0

    for n in nums:
        if n == 0:
            c0 += 1
        elif n == 1:
            c1 += 1
        else:
            c2 += 1
    indx = 0
    for i in range(c0):
        nums[indx] = 0
        indx += 1
    
    for i in range(c1):
        nums[indx] = 1
        indx += 1
    
    for i in range(c2):
        nums[indx] = 2
        indx += 1

num = [1,2,0,1,2,1,0,0,2,1]
dutchFlagProblem(num)
print(num)
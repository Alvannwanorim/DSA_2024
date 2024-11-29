def longestPerm(nums, b):
    # @param nums: list of integers
    # @param a: integer
    # @return a list of integers
    i = 0
    _max = len(nums)
    d = {x:i for i, x in enumerate(nums)}

    while b and i < len(nums):
        j= d[_max]
        print(i,j)
        if i == j:
            continue
        else:
            b -= 1
            nums[i], nums[j]= nums[j], nums[i]
            d[nums[i]], d[nums[j]] = d[nums[j]], d[nums[i]]
        i += 1
        _max -= 1
    return nums

print(longestPerm([3,2,4,1,5],3))
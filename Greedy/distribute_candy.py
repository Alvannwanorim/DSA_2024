def candy(nums):
    n= len(nums)
    data = sorted((x,i) for i,x in enumerate(nums))
    candies = [1] * n

    for _, i in data:
        if i > 0 and nums[i] > nums[i-1]:
            candies[i] = max(candies[i], candies[i-1] + 1)
        
        if i < n -1 and nums[i] > nums[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)

def separateEvenOdd(nums):
    left = 0
    right = len(nums) -1 
    while left < right:
        while (nums[left] % 2 == 0 and left < right):
            left += 1

        while (nums[right] % 2 == 1 and left < right):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
nums = [16,16,19,20,25,1,3,4,5,7,10,14]
separateEvenOdd(nums)
print(nums)


            
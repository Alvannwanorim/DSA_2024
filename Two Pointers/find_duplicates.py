from typing import List


def removeDuplicates(nums:List[int]):
    m = 0
    for i in range(len(nums)):
        if(not elem(nums, m, nums[i])):
            nums[m] = nums[i]
            m += 1
        return m

def elem(nums: List[int], n, e):
    for i in range(n):
        if nums[i] == e:
            return 1
    return 0



def removeDuplicates2(nums: List[int]):
    nums.sort()
    j = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] =nums[i]
            j += 1
    return j

nums = [1,2,3,2,3,4,4,5,5,6]
print(removeDuplicates2(nums))
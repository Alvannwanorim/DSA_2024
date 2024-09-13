from typing import List

def permutation(nums: List[int]):
    res = []
    # base case 
    if len(nums) == 1:
        return [nums[:]] # deep copy of nums
    
    for i in range(len(nums)):
        n= nums.pop(0)
        perms = permutation(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

print(permutation([1,2,3,4]))

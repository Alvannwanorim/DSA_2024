from typing import List
def pairSum(nums: List[int], target: int):
    res  = []
    table = {c:c for c in nums}
    print(table)
    for n in nums:
        diff = target - n 
        if diff in table:
            res.append([diff, n])
    
    return res

print(pairSum([1,2,4,5,2,5,3],6))


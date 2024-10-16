from typing import List


def symmetricPairs(nums: List[List[int]]):
    table = {}
    res = []
    for k, v in nums:
        table[k] = v
        if v in table and table[v] == k:
            res.append([k,v])
    return res

print(symmetricPairs([[1,2],[2,1],[3,5], [7,6],[5,3]]))

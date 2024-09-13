from typing import List
def all_sum(target: int, nums: List[int]):
    def dfs(target, nums): 
        if target == 0:
            return [[]]
        if target  < 0: 
            return []
        result = []
        for n in nums:
            diff = target - n 
            combinations = dfs(diff, nums)
            for comb in combinations:
                # print(comb)
                result.append(comb + [n])
        return result

    return dfs(target, nums)

print(all_sum(7, [1,9,5,4,6,7]))
    

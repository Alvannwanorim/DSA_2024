from typing import List
def best_sum(target: int, nums: List[int]):
    def dfs(target, nums): 
        if target == 0:
            return []
        if target < 0: 
            return 
        shortest = None 
        for n in nums:
            combinations = dfs(target - n, nums)
            if combinations is not None:
                result = combinations + [n]
            if shortest is None or (len(result) <= shortest):
                shortest = len(result)
        return shortest
    return dfs(target, nums)


print(best_sum(7, [1,9,5,4,6,7]))
    


        
        
from typing import List


class Solution:
    def carFleet(seld,position:List[int], speed: List[int], target:int):
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []
        for p,s in pairs:
            stack.append((target - p)/ s)
            print(stack)
            if len(stack) >1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

sol = Solution()
print(sol.carFleet( [10,8,0,5,3],[2,4,1,1,3], 12))
print(sol.carFleet( [0,2,4], [4,2,1],100))
print(sol.carFleet( [3],[23], 10))
"""
"""
from typing import List

def travelPaths(r: int, c: int, memo={}):
    if (r,c) in memo:
        return memo[(r,c)]
    if r== 1 and c == 1:
        return 1
    if r ==0 or c == 0: return 0
    memo[(r,c)] = travelPaths(r -1, c) + travelPaths(r, c - 1)
    return memo[r,c]
    

        
def travelPathsTwo(grid: List[List[int]]):
    ROW, COL = len(grid), len(grid[0])

    def  dfs(r,c):
        if r == ROW-1 and c == COL-1:
            return 1
        if r >= ROW  or c >= COL:
            return 0
        return dfs(r + 1, c) + dfs(r, c+1)
    
    return dfs(0,0)
    # visited = set()
grid = [
    [1, 2, 3, 4],
    [4, 6, 7, 8],
    [0, 2, 4, 5]
]


print(travelPaths(3,4))
print(travelPathsTwo(grid))
print(travelPaths(15,15))
print(travelPaths(18,18))
# print(travelPaths(6,6))
# print(travelPaths(10,10))
# print(travelPaths(15,15))
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= ROW or \
            c >= COL or grid[r][c] == "0" or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c) 
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)
        
        num_of_islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print("here")
                    num_of_islands += 1
                    dfs(grid, r,c)
                   
        return num_of_islands
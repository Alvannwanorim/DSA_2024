from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= ROW or \
            c >= COL or grid[r][c] == 0 or (r,c) in visited:
                return 0  
            visited.add((r,c))
            return 1 + dfs(grid, r - 1, c) \
            + dfs(grid, r + 1, c) + dfs(grid, r, c - 1) \
             + dfs(grid, r, c + 1)
        
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(grid, r,c)
                    max_area = max(area,max_area)
        return max_area
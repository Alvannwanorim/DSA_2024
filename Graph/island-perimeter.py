from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(grid, r, c):
            if r <0 or c <0 or r >= len(grid) \
            or c >= len(grid[0]) or  grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perim = 0
            perim += dfs(grid, r-1,c)
            perim += dfs(grid, r+1,c)
            perim += dfs(grid, r,c - 1)
            perim += dfs(grid, r,c + 1)

            return perim
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(grid, r,c)
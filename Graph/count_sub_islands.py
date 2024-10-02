from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROW, COL = len(grid1), len(grid1[0])
        visited = set()
        sub_islands = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROW or c== COL or (r,c) in visited or grid2[r][c] == 0):
                return True
            res = True
            if grid1[r][c] == 0:
                res = False
            visited.add((r,c))
            res =dfs(r + 1,c) and res
            res = dfs(r - 1,c) and res
            res = dfs(r,c + 1) and res
            res = dfs(r,c - 1) and res
            return res
        for r in range(ROW):
            for c in range(COL):
                if grid2[r][c] == 1 and (r,c) not in visited and dfs(r,c):
                    sub_islands += 1

        return sub_islands

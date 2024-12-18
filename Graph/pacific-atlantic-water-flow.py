from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        atl = set()
        pac = set()
        def dfs(r,c,visited, prevHeight):
            if ((r,c) in visited or r < 0 
            or c < 0 or r == ROW or c == COL
            or heights[r][c] < prevHeight):
                return 
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1,c, atl, heights[ROW - 1][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        
        return res

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0
        time = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])

        directions = [[0, 1],[0, -1], [1, 0],[-1, 0]]
        
        while fresh > 0 and q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    if(row < 0 or col < 0 or row >= ROW or col >= COL 
                    or (row,col) in visited or grid[row][col] == 0):
                        continue
                    
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if not fresh  else -1 

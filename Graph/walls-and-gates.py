from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()

        def addRoom(r,c):
            if (min(r,c) < 0) or r == ROW or c == COL or (r,c) in visited or rooms[r][c] == -1:
                return 
            visited.add((r,c))
            queue.append([r,c])

            
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r + 1,c)
                addRoom(r - 1,c)
                addRoom(r,c + 1)
                addRoom(r,c -1)
            
            dist += 1
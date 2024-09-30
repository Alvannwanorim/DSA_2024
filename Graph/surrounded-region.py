from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        visited = set()
        def capture(r,c):
            if (min(r,c) < 0 or r == ROW or c == COL 
            or (r,c) in visited or board[r][c] != "O" ):
                return 
            board[r][c] = "T"
            visited.add((r,c))
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O" and r in [0, ROW - 1] or c in [0, COL - 1]:
                    capture(r,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] ="O"
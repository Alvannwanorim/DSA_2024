from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        # if(top <= bot):
        #     return False
        row = (top + bot) // 2
        l,r = 0, COLS -1 
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False 

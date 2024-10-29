from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table = [[1]]

        for i in range(numRows -1):
            plot = [0] + table[-1] + [0]
            temp = []
            for j in range(len(plot) - 1):
                temp.append(plot[j] + plot[j+1])
            table.append(temp)
        return table


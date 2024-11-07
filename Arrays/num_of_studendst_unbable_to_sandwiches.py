from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        res = len(students)
        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1 
            else:
                return res
        return res
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {crs: [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            preq[crs].append(pre)
        cycle =set()
        visited = set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)

            for pre in preq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {crs:[] for crs in range(numCourses)}
        visiting = set()
        for crs, pre in prerequisites:
            preq[crs].append(pre)
    
        def dfs(crs):
            if crs in visiting:
                return False
            if preq[crs]== []:
                return True
            
            visiting.add(crs)

            for pre in preq[crs]:
                if dfs(pre) == False:
                    return False
            visiting.remove(crs)
            preq[crs]= []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True
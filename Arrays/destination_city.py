from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        dist = set()

        for s,d in paths:
            source.add(s)
            dist.add(d)
        
        for d in dist:
            if d not in source:
                return d
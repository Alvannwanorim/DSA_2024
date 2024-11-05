class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {
            "N": (0,1),
            "S": (0,-1),
            "W": (-1,0),
            "E": (1,0),
        }
        x, y = 0,0
        visit = set()
        for p in path:
            visit.add((x,y))
            dx, dy = dirs[p]
            x, y = x + dx, y + dy
            print((x,y),(dx,dy),p)
            if (x,y) in visit:
                return True
            
        return False
        
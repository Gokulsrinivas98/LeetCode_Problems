class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = {
            'N': (0,1),
            'S': (0,-1),
            'E': (1,0),
            'W': (-1,0)
        }
        x,y = 0,0
        visited = [(0,0)]
        for i in path:
            dx,dy = paths[i]
            x+=dx
            y+=dy
            
            if (x,y) in visited:
                return True
            visited.append((x,y))
        return False
    
    
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = 2**31 - 1
        point_set = set()
        for x,y in points:
            point_set.add((x,y))
        
        for x1,y1 in points:
            for x2,y2 in points:
                if (x1,y2) in point_set and (x2,y1) in point_set:
                        area = abs(x1-x2)*abs(y1-y2)
                        if area:
                            min_area = min(min_area,area)
        return 0 if min_area == 2**31 -1 else min_area
            
        
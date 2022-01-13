class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        r, shoot = 0, float('inf')
        for s, e in sorted(points, reverse = True):            
            if shoot > e:
                shoot = s
                r += 1
        return r
        
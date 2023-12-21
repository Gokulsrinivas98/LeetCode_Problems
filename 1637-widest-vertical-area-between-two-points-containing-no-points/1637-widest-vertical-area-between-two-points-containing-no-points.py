class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = list(set(x for x,_ in points))
        if len(xs) == 1: return 0
        xs.sort()
        return max(xs[i]-xs[i-1] for i in range(len(xs)))
                   
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return False if t == 1 and sx == fx and sy == fy else max(abs(fy-sy),abs(fx-sx)) <= t
    
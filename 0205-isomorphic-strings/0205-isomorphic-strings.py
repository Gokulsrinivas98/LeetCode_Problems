class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = [s.index(i) for i in s]
        t_map = [t.index(i) for i in t]
        return s_map == t_map
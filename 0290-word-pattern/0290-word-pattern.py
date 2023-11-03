class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        if len(pattern) != len(l):
            return False
        p_map = [pattern.index(i) for i in pattern]      
        s_map = [l.index(i) for i in l]
        return p_map == s_map
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = [pattern.index(i) for i in pattern]
        l = list(s.split())
        s_map = [l.index(i) for i in l]
        print(p_map)
        print(s_map)
        return p_map == s_map
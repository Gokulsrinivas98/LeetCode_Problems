class Solution:
    def firstUniqChar(self, s: str) -> int:
        for str in s:
            if s.count(str) == 1:
                return s.index(str)
        return -1
        
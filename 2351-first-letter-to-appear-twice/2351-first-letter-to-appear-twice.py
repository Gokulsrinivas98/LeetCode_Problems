class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = [0]*26
        for c in s:
            if res[ord(c) - ord('a')]: return c
            res[ord(c) - ord('a')] = True
        return 'a'
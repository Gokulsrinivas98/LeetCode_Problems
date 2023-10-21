class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for i in s:
            c ^= ord(i)
        for i in t:
            c ^= ord(i)
        return chr(c)

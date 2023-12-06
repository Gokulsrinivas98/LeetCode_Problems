class Solution:
    def titleToNumber(self, cT: str) -> int:
        n = 0
        for i in cT:
            d = ord(i)-64
            n = n*26+ d
        return n
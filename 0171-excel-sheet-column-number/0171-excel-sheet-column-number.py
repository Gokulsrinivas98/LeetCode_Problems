class Solution:
    def titleToNumber(self, cT: str) -> int:
        n = 0
        for i in cT:
            n = n*26+(ord(i)-64)
        return n
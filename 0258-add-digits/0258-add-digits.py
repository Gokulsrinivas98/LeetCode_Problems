class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num:
            s += num%10
            num = num//10
        if s < 10:
            return s
        else:
            return self.addDigits(s)
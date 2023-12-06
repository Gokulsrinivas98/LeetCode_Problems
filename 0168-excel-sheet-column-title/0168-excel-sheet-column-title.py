class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n>0:
            n-=1
            curr = n % 26
            n = int(n / 26)
            s+=chr(curr + ord('A'))
        return s[::-1]
            
        
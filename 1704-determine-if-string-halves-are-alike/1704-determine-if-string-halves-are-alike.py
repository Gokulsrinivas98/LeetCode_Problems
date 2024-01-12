class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        av,bv = 0,0
        v = "aeiou"
        a,b = s[:n//2].lower(), s[n//2:].lower()
        for i in range(n//2):
            if a[i] in v : av +=1
            if b[i] in v : bv +=1
        return av == bv
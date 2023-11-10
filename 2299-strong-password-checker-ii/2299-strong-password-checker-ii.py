class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8 : return False
        prev = ''
        lc = uc = d = sc = 0
        for n in password:
            if prev == n: return False
            if n.isdigit(): d = 1
            if n.islower(): lc = 1
            if n.isupper(): uc = 1
            if n in "!@#$%^&*()-+": sc = 1
            prev = n    
        return d + lc + uc + sc == 4 
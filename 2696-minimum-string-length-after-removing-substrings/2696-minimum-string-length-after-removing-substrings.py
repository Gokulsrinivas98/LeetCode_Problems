class Solution:
    def minLength(self, s: str) -> int:
        # while s:
        #     if "AB" not in s and "CD" not in s:
        #         return len(s)
        #     elif "AB" in s:
        #         s=s.replace("AB",'')
        #     elif "CD" in s:
        #         s=s.replace("CD",'')
        
        while "AB" in s or "CD" in s:
            s = s.replace("AB",'').replace("CD",'')
        return len(s)
class Solution:
    def romanToInt(self, s: str) -> int:
        rome = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        result = 0
        for i in range(len(s)):
            if i < (len(s) - 1) and rome[s[i]] < rome[s[i+1]]:
                result -=rome[s[i]]
            else:
                result+= rome[s[i]]
        return result
            
        
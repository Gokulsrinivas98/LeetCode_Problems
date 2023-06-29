class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if not s:
                return True
            if 'abc' not in s:
                break
            s = re.sub('abc', '', s)           
            
        return False
        
        
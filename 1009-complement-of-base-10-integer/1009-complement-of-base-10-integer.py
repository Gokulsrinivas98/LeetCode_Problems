class Solution:
    def bitwiseComplement(self, n: int) -> int:
        temp = 1
        while n > temp:
            
            temp = temp * 2 + 1
            
        return temp - n    
        
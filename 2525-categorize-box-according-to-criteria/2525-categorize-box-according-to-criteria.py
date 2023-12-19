class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        idx = int( length*width*height >= 10**9 or length+width+height >= 10**4) + 2*( mass>=100)
        return ('Neither','Bulky','Heavy','Both')[idx] 
        
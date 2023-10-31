class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # return [[i,n-i] for i in range(n,-1,-1) if '0' not in str(i) and '0' not in str(n-i)][0]
        a,b = 1,n-1
        while '0' in str(a) or '0' in str(b):
            a,b = a+1,b-1
        return [a,b]
            
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return [[i,n-i] for i in range(n,-1,-1) if '0' not in str(i) and '0' not in str(n-i)][0]
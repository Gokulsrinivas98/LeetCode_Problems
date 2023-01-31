class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [1]
        for _ in range(rowIndex):
            a = [x+y for x,y in zip([0]+a,a+[0])]
        return a
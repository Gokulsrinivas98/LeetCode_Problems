class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        x,y = arr[0][0],arr[0][1]
        dx,dy = arr[1][0]-x, arr[1][1]-y
        n = len(arr)
        for i in range(n):
            if dx * (arr[i][1] - y) != dy * (arr[i][0] - x):
                return False
        return True
class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        x,y = arr[0][0],arr[0][1]
        dx,dy = arr[1][0]-x, arr[1][1]-y
        n = len(arr)
        for xn,yn in arr:
            if dx * (yn - y) != dy * (xn - x):
                return False
        return True
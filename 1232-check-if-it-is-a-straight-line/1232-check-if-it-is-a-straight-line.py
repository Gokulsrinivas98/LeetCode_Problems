class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        x1,y1 = arr[0]
        x2,y2 = arr[1]
        
        for xn,yn in arr:
            if (xn - x2) * (yn - y1) != (yn-y2) * (xn - x1):
                return False
        return True
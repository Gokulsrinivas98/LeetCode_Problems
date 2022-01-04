class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        p,v = 0,0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                p += 1
            elif arr[i-1] >= arr[i] <= arr[i+1]:
                v += 1
        return p == 1 and v == 0        
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == 2*arr[j] and i != j:
                    print(arr[i],arr[j])
                    return True
        return False        
        
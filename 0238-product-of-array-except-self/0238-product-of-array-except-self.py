class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,left,right = len(nums),1,1
        res = [1]*n
        i,j = 1,n-2
        while i < n and j > -1:
            left *= nums[i-1]
            right *= nums[j+1]
            res[i] *= left
            res[j] *= right
            i += 1
            j -= 1
        return res
        

        
        
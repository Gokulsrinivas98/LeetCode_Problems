class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right =1,1
        output = [1]*n
        
        for i in range(1,n):
            left *= nums[i-1]
            output[i] *= left
        
        for i in range(n-2,-1,-1):
            right *= nums[i+1]
            output[i] *= right
        return output
        
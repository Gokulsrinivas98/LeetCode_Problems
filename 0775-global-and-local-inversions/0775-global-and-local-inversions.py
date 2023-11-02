class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # global_inv, local_inv = 0,0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] > nums[j]:
        #             global_inv += 1
        #     if i != n-1 and nums[i] > nums[i+1]:
        #         local_inv += 1
        # return global_inv == local_inv
        
        for i,v in enumerate(nums):
            if abs(i-v) > 1:
                return False
        return True
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,m, zero = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                while zero > 1:                    
                    if nums[l] == 0:
                        zero -= 1
                    l = l+1    
            m = max(m, i-l+1 )            
        return m
            
            

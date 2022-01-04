class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = 0
        l = [0]
        for i in range(len(nums)):
            if nums[i] == 1:
                s = s+1
            else:
                l.append(s)
                s = 0
                
        return max(s,max(l))        
                
        
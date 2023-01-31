class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0  
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                c +=1
            else:
                nums[i-c] = nums[i]

        return len(nums)-c        
            
        
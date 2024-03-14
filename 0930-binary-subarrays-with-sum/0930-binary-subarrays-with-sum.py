class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = count = result = s = 0
        for right,value in enumerate(nums):
            s += value
            if value == 1: count = 0
            while left <= right and s>= goal:
                if s == goal: count += 1
                s -= nums[left]
                left += 1
            result += count
                
        return result
     
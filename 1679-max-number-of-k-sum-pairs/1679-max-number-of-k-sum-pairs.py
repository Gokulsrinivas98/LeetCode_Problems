class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        start = 0
        end = len(nums)-1
        nums.sort()
        while start < end:
            if nums[start] + nums[end] == k:
                start += 1
                count += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
        return count
    
     
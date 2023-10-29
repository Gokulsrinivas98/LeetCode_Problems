class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        start = 0
        end = len(nums)-1
        nums = sorted(nums)
        while start < end:
            ns = nums[start]
            ne = nums[end]
            if ns + ne == k:
                start += 1
                count += 1
                end -= 1
                continue
            if ns + ne < k:
                start += 1
            else:
                end -= 1
        return count
    
     
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for j in range(n):
            for i in range(0,j):
                if abs(nums[i]-nums[j]) == k: count += 1
        return count
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]
        nums.sort()
        return nums[len(nums)//2]
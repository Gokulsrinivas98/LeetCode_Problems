class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c =0
        for i in range(len(nums)):
            if nums[i] ==100000 or nums[i] > 999 and nums[i] <=9999 or nums[i] > 9 and nums[i] <=99:
                c = c+1
        return c
                
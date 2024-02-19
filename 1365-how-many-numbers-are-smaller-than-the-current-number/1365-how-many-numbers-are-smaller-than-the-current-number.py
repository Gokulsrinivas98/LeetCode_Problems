class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n2 = sorted(nums)
        return [n2.index(i) for i in nums]
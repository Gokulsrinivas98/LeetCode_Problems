class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        return (sortednums[-1]*sortednums[-2])-((sortednums[0]*sortednums[1]))
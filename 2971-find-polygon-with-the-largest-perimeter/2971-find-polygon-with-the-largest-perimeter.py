class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        peri = sum(nums)
        while peri and peri <= nums[-1]*2:
            peri -= nums.pop()
        return sum(nums) if len(nums) > 2 else -1
            
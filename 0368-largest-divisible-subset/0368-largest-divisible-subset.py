class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp =[[]]
        for i in sorted(nums):
            dp.append([i] + max((s for s in dp if not s or i%s[0]==0),key=len))
        return max(dp,key = len)
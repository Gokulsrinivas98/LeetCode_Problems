class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for i in range(n-1):
            s = nums[i]+nums[i+1]
            if s in seen:
                return True
            seen.add(s)
        return False
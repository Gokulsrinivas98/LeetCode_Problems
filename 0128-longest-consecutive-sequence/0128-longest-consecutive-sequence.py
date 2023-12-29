class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums.sort()

        n,res,v = len(nums),0,1
        for i in range(1,n):
            if nums[i] == nums[i - 1] : continue
            elif nums[i] == nums[i - 1]+1: v+=1
            else:
                res = max(res,v)
                v = 1
        return max(res,v)
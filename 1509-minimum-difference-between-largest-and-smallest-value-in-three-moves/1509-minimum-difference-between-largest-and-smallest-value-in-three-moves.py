class Solution:
    def minDifference(self, nums: List[int]) -> int:
#         if len(nums) <= 4:
#             return 0
        
#         mini = min(nums)
#         maxi = max(nums)
        
#         nums.sort(reverse=True)
#         nums2 = sorted(nums)

#         for i in range(3):
#             nums[i] = mini
#             nums2[i] = maxi
#         return min(max(nums)-min(nums),max(nums2)-min(nums2)) 

        if len(nums) <= 4: return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])
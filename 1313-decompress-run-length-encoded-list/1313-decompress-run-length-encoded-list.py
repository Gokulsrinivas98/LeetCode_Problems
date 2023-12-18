class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(0,n,2):
            freq = nums[i]
            val = nums[i+1]
        #     for j in range(freq):
        #         res.append(val)
        # return res
            res += [val]*freq
        return res
    
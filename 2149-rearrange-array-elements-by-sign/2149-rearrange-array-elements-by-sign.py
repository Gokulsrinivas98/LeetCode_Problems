class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = [i for i in nums if i > 0]
#         neg = [i for i in nums if i < 0]
        
#         res = []
#         for i,j in zip(pos,neg):
#             res.append(i)
#             res.append(j)
#         return res
        n = len(nums)
        pos,neg = 0,1
        res = [0]*n
        for i in range(n):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos+=2
            else:
                res[neg] = nums[i]
                neg+=2
        return res
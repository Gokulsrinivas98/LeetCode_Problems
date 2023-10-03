class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        res = 0
        for i in count:
            if i+1 in count:
                res = max(res,count[i]+count[i+1])
        return res
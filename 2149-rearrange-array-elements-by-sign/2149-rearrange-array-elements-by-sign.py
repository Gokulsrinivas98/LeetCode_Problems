class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        
        res = []
        for i,j in zip(pos,neg):
            res.append(i)
            res.append(j)
        return res
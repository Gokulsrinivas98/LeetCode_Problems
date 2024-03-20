class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = {}
        for i in sorted(arr):
            res.setdefault(i,len(res)+1)
        return map(res.get,arr)

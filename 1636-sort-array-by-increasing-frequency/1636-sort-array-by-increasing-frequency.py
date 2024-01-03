class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
#         dic = Counter(nums)
        
#         f = sorted([(v,k) for k,v in dic.items()], key=lambda x:x[0])
#         res = []
#         for v,k in f:
#             res2 = [k]*v
#             res += res2
            
            
#         return res

        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
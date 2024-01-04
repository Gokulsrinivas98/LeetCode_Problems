class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
        res = 0
        for t in c.values():
            if t == 1:
                return -1
            res += t // 3
            if t % 3:
                res += 1
                
        return res
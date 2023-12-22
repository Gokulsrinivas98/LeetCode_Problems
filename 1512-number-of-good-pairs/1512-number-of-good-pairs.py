class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        rep = collections.defaultdict(int)
        res = 0
        for num in nums:
            res += rep[num]
            rep[num] += 1
        return res
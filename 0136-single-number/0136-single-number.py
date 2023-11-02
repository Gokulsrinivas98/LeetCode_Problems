class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common()[-1][0]
        s = 0
        for i in nums:
            s = s^i
        return s
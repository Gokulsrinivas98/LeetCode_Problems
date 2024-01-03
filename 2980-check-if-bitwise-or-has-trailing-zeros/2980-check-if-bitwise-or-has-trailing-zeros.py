class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evn = 0
        for i in nums:
            if i % 2 == 0: evn+=1
            if evn >= 2: return True
        return False
            
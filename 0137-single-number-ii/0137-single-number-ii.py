class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
        
        # c = Counter(nums)
        # for i in c:
        #     if c[i] !=3:
        #         return i
        # return -1
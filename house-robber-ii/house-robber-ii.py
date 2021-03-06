class Solution:
    def rob(self, nums: List[int]) -> int:
        def Houserobber(nums):
            prev, curr = 0,0
            for n in nums:
                t = prev
                prev = curr
                curr = max(n+t,prev)
            return curr
    
        if len(nums) == 1:
            return(nums[0])
        elif len(nums) == 2:
            return(max(nums[0],nums[-1]))
        else:
            return(max(Houserobber(nums[1:]), Houserobber(nums[:-1])))
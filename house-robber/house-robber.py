class Solution:
    def rob(self, nums: List[int]) -> int:
    
        prev, curr = 0,0
        for n in nums:
            t = prev
            prev = curr
            curr = max(n+t,prev)
        return curr          
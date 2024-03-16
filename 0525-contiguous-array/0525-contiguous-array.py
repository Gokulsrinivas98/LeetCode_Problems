class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count,max_l = 0,0
        table = {0:0}
        for ind,val in enumerate(nums,1):
            if val == 0: count -=1
            else: count += 1 
            if count in table: max_l = max(max_l,ind - table[count])
            else: table[count] = ind
        return max_l

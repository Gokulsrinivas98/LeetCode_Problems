class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(index)
        target = []
        for i in range(n):
            target.insert(index[i],nums[i])
        return target
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i in c.keys() if c[i] > 1]
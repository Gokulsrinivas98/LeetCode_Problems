class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap[comp],i]
            hashmap[nums[i]] = i
        return []
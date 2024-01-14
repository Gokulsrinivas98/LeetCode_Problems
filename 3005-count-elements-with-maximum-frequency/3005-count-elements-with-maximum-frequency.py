class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            maps[i] = maps.get(i,0) + 1
        
        maxi = 0
        count = 0
        for key,value in maps.items():
            maxi = max(maxi,value)
        for key,value in maps.items():
            if maxi == value:
                count += value
        return count
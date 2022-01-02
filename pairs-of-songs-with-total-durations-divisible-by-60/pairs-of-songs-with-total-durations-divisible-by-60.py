class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = 0
        arr = [0] * 60
        for t in time:
            
            c += arr[-t % 60]
            arr[t % 60] += 1
            
        return c
        
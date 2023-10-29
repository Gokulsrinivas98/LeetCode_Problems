class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        for i in range(len(gain)):
            result.append(result[-1]+gain[i])
        return max(result)
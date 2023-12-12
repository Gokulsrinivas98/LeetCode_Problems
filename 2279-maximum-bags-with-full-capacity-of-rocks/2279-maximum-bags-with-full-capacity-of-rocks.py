class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        sub = sorted(capacity[i]-rocks[i] for i in range(n))[::-1]
        while sub and additionalRocks and sub[-1] <= additionalRocks:
            additionalRocks -= sub.pop()
        return len(rocks)-len(sub)
    
        
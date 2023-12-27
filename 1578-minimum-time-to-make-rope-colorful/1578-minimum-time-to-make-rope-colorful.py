class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost_max = res = 0 
        
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                cost_max = 0
            res += min(cost_max,neededTime[i])
            cost_max = max(cost_max,neededTime[i])
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = max_p = i = 0
        n = len(prices)-1
        while i < n:
            while i < n  and prices[i+1] <= prices[i]:
                i += 1
            buy = prices[i]
            while i < n and prices[i+1] > prices[i]:
                i +=1
            sell = prices[i]
            max_p += sell-buy
        return max_p
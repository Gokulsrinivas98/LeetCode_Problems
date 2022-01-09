class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof, min_price = 0 , float('inf')
        for i in prices:
            min_price = min(i,min_price)
            prof = i - min_price
            max_prof = max(max_prof, prof)
        return max_prof
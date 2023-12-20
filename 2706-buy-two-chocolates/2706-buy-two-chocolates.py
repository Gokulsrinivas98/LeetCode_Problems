class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a = prices[0]+prices[1]
        print (a)
        return money - a if a <= money else money
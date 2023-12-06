class Solution:
    def accountBalanceAfterPurchase(self, pA: int) -> int:
        return 100 - (((pA+5)//10)*10)
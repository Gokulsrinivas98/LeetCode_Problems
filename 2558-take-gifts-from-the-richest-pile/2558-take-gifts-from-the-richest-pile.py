class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # for _ in range(k):
        #     # a = max(gifts)
        #     # index = gifts.index(a)
        #     gifts[gifts.index(max(gifts))]= int((max(gifts))**0.5)
        # return sum(gifts)
        
        gifts = [-i for i in gifts]
        heapify(gifts)
        for _ in range(k):
            num = math.isqrt(-heappop(gifts))
            heappush(gifts,-num)
        return -sum(gifts)
            
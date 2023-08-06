class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # result = [0]*len(candies)
        # for i in range(0, len(candies)):
        #     if candies[i] + extraCandies >= max(candies):
        #         result[i] = True
        # return result
        result = []
        n = max(candies)
        for i in candies:
            if i+extraCandies >= n:
                result.append(True)
            else:
                result.append(False)
        return result
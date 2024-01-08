class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        max_d, max_a = 0, 0
        for l, w in d:
            d = l ** 2 + w ** 2
            if d > max_d:
                max_d = d
                max_a = l * w
            elif d == max_d and l * w > max_a:
                max_a = l * w

        return max_a

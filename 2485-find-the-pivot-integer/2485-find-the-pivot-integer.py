class Solution:
    def pivotInteger(self, n: int) -> int:
        elements = list(range(1, n+1))
        for i in range(n):
            if sum(elements[:i+1]) == sum(elements[i:]):
                return i+1
        return -1
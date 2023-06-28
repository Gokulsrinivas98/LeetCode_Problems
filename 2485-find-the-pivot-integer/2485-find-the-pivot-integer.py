class Solution:
    def pivotInteger(self, n: int) -> int:
        elements = []
        for  i in range(1,n+1):
            elements.append(i)
        for i in range(n):
            if sum(elements[:i+1]) == sum(elements[i:]):
                return i+1
        return -1
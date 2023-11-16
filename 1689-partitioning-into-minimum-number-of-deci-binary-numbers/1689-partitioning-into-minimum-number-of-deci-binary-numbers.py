class Solution:
    def minPartitions(self, n: str) -> int:
        s = 0
        for i in n:
            if int(i) > s:
                s = int(i)
        return s
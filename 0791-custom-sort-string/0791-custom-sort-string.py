class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []
        for i in order:
            if i in count:
                res.extend([i]*count[i])
                count.pop(i)
        for key,value in count.items():
            res.extend(key*value)
        return ''.join(res)
        
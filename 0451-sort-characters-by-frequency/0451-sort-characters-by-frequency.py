class Solution:
    def frequencySort(self, s: str) -> str:
        # c = Counter(s)
        # s = list(s)
        # s.sort(key=lambda x:(-c[x],x))
        # return ''.join(s)
        dic = Counter(s)
        
        f = sorted([(v,k) for k,v in dic.items()], key=lambda x:x[0], reverse=True)
        res = ''
        for v,k in f:
            res+=k*v
            
        return res
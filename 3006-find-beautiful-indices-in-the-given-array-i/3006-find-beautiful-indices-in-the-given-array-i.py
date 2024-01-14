class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        slen = len(s)
        alen = len(a)
        blen = len(b)
        res = []
        i_idx,j_idx = [],[]
        for i in range(slen-alen+1):
            if s[i : i + alen] == a:
                i_idx.append(i)
                
        for j in range(slen-blen+1):
            if s[j : j + blen ] == b:
                j_idx.append(j)
        
        for i in i_idx:
            for j in j_idx:
                if abs(j-i) <= k:
                    res.append(i)
                    break
                        
        return res
                        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=[]
        l=len(p)
        cp=Counter(p)
        cs=Counter(s[:l-1])
        i=0
        while i+l<=len(s):
            cs[s[i+l-1]]+=1
            if cs==cp:
                a.append(i)
            cs[s[i]]-=1
            if cs[s[i]]==0:
                del cs[s[i]]
            i+=1
        return a
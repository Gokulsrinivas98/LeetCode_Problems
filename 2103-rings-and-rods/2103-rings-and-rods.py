class Solution:
    def countPoints(self, rings: str) -> int:
        r,g,b = [],[],[]
        for i in range(0,len(rings),2):
            if rings[i] == 'R':
                r.append(rings[i+1])
            elif rings[i] == 'G':
                g.append(rings[i+1])
            elif rings[i] == 'B':
                b.append(rings[i+1])
        print(r,g,b)
        common = set(r) & set(g) & set(b)
        return len(list(common)) if common else 0 
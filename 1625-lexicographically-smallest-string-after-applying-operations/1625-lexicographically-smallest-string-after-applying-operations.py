class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotate(s,b):
            return s[len(s)-b:]+s[:len(s)-b]
        
        def add(s,a):
            new = ''
            for i in range(len(s)):
                if i % 2 != 0:
                    k = int(s[i]) + a
                    if k > 9:
                        k -= 10
                    new += str(k)
                else:
                    new += s[i]
            return new
        
        seen = set()
        l = list()
        l.append(s)
        
        while l:
            curr = l.pop()
            if curr not in seen:
                seen.add(curr)
                l.extend([add(curr,a),rotate(curr,b)])
        return min(seen)
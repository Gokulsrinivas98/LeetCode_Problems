class Solution:
    def finalString(self, s: str) -> str:
        # s = list(s)
        # start = 0
        # while start < len(s):
        #     if s[start] == 'i':
        #         s[0:start] = s[0:start][::-1]
        #         s.remove(s[start])
        #         start -=1
        #     start +=1
        # return "".join(s)
        
        o = []
        for c in s:
            if c != 'i':
                o.append(c)
            else:
                o = o[::-1]
        return "".join(o)
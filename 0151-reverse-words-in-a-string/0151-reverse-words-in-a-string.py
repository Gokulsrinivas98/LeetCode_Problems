class Solution:
    def reverseWords(self, s: str) -> str:
        rs = []
        r = []
        for i in s:
            if i != ' ' : 
                r.append(i)
            else:
                rs.insert(0,r)
                r = []
        rs.insert(0,r)
        return ' '.join([''.join(sublist) for sublist in rs if sublist != []])
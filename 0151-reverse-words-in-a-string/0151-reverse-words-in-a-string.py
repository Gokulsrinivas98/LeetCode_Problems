class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        rs = []
        while words:
            w = words.pop()
            if w.strip() == '':
                continue
            rs.append(w)
        return ' '.join(rs)
    
        # rs = []
        # r = []
        # for i in s:
        #     if i != ' ' : 
        #         r.append(i)
        #     else:
        #         rs.insert(0,r)
        #         r = []
        # rs.insert(0,r)
        # return ' '.join([''.join(sublist) for sublist in rs if sublist != []])
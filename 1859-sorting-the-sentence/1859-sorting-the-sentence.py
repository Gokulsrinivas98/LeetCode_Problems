class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s_list = [0]*len(s)
        for i in s:
            s_list[int(i[-1]) - 1] = i[0:-1]
        return " ".join(s_list)
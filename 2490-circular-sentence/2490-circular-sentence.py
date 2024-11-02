class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        split = sentence.split()
        for  i in range(len(split)):
            if split[i-1][-1] != split[i][0]:
                return False
        return True
        
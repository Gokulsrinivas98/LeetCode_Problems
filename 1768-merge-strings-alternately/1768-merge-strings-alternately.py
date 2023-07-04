class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=""
        for i,j in zip(word1,word2):
            word3 += i+j
        
        if len(word1) > len(word2):
            return word3+ word1[len(word2):]
        elif len(word2) > len(word1):
            return word3+ word2[len(word1):]
        else:
            return word3
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # i=0
        # while i < len(words)-1:
        #     if Counter(words[i]) == Counter(words[i+1]):
        #         words.remove(words[i+1])
        #     else:
        #         i+=1
        # return words
        res = []
        prev = ''
        for i in words:
            sort_i = sorted(i)
            if sort_i != prev:
                res.append(i)
            prev = sort_i
        return res
        
            
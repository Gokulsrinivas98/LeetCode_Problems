class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0
        for i in range(len(words)):
            chars_i = set(words[i])
            for j in range(i+1,len(words)):
                if not chars_i.intersection(set(words[j])):
                # if set(words[i]).isdisjoint(set(words[j])):
                    count = len(words[i])*len(words[j])
                    maxi= max(count,maxi)
                
        return maxi
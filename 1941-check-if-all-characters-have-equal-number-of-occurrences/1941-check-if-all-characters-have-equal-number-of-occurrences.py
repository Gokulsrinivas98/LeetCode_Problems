class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # return len(set([Counter(s)[i] for i in Counter(s)])) == 1
        c1 = Counter(s)
        
        lst = [c1[i] for i in c1]        
        return all(element == lst[0] for element in lst[1:])
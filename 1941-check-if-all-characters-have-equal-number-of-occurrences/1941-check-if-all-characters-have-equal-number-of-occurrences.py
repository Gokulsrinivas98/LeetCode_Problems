class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c1 = Counter(s)
        lst = [c1[i] for i in c1]        
        return all(element == lst[0] for element in lst[1:])
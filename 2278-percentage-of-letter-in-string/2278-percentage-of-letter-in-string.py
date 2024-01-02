class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = Counter(s)
        if letter not in c.elements():
            return 0
        else: 
            return int((c[letter]/len(s))*100)
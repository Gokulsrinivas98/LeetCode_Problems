class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = ''.join([' ' if not c.isdigit() else c for c in word])
        return len({int(char) for char in set(word.split())})
        
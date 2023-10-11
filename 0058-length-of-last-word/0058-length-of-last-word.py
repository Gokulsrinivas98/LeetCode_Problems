class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return int(len(str(s.strip().split(' ')[-1])))
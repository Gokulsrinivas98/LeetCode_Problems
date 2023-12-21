class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pr = ''
        l = len(s)
        for i in words:
            pr += i
            if pr == s:
                return True
            elif len(pr) > l:
                return False
            
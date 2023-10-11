class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        needlen = len(needle)
        for i in range(haylen):
            if haystack[i:i+needlen] == needle:
                return i
        return -1
            
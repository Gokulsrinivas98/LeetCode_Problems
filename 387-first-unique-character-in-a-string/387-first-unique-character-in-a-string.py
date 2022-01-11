class Solution:
    def firstUniqChar(self, s: str) -> int:
#         for str in s:
#             if s.count(str) == 1:
#                 return s.index(str)
#         return -1
        alp = 'abcdefghijklmnopqrstuvwxyz'
        ind = [s.index(char) for char in alp if s.count(char) == 1]
        return min(ind) if len(ind) > 0 else -1
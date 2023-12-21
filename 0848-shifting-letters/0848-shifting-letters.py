class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
#         s = list(s)
#         n = len(shifts)
        
#         for i in range(n):
#             for j in range(i+1):
#                 s[j] = chr((ord(s[j]) - 97 + shifts[i]) % 26 + 97)
#         return ''.join(s)
        ans, shift = '', 0
        for i in range(len(shifts) -1, -1, -1):
            ans += chr((ord(s[i]) - ord('a') + shift+shifts[i]) % 26 + ord('a'))
            shift += shifts[i]
        
        return ans[::-1]

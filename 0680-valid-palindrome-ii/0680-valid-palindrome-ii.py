class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i+1:j+1]
                print(delete_i)
                delete_j = s[i:j]
                print(delete_j)
                return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]
            i += 1
            j -= 1
        return True
    
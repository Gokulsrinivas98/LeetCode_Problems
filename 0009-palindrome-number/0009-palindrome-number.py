class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        reversed_number = str(x)[::-1]
        return x == int(reversed_number)
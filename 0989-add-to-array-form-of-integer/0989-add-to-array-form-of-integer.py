class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # num = int(''.join([str(n) for n in num]))
        n = num[0]
        for i in range(1,len(num)):
            n = n*10 + num[i]
        
        n = n+k
        digits = []
        while n > 0:
            digit = n % 10
            digits.insert(0, digit)  # Insert the digit at the beginning of the list
            n //= 10
        return digits
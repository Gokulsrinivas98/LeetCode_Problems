class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int(''.join([str(dig) for dig in digits]))
        digit+=1
        return [int(dig) for dig in str(digit)]
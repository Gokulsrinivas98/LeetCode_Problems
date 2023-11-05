class Solution:
    def minInsertions(self, s: str) -> int:
        left = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    left += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0 :
                    right += 2
                    left += 1 
        return left + right                   
        
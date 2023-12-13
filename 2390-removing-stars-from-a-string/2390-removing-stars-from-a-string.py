class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in s:
            if i == '*':
                stack.pop()
                
            else:
                stack.append(i)
        return ''.join(stack)
            
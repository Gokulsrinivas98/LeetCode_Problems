class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)
            
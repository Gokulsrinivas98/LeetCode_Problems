class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeStars(sa):
            stack = []
            n = len(sa)
            for i in sa:
                if i == '#' and stack:
                    stack.pop()

                elif i != '#':
                    stack.append(i)
            return  ''.join(stack)
        return removeStars(s) == removeStars(t) 
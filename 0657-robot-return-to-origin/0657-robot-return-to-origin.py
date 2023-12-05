class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = [0,0]
        for i in moves:
            if i == 'U':
                c[0] += 1
            elif i == 'D':
                c[0] -= 1
            elif i == 'R':
                c[1] += 1
            else:
                c[1] -= 1
        return c == [0,0]
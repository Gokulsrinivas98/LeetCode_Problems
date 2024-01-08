class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
           # rock and queen in the same row or col
        if a == e: # same row
            if a == c and (d - b) * (d - f) < 0: # bishop on the same row and between rock and queen
                return 2
            else:
                return 1
        elif b == f: # same col
            if b == d and (c - a) * (c - e) < 0:
                return 2
            else:
                return 1
        # bishop and queen in the same diagonal
        elif c - e == d - f: # \ diagonal
            if a - e == b - f and (a - c) * (a - e) < 0:
                return 2
            else:
                return 1
        elif c - e == f - d: # / diagonal
            if a - e == f - b and (a - c) * (a - e) < 0:
                return 2
            else:
                return 1
        return 2
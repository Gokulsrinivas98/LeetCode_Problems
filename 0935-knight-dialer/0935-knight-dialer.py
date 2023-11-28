class Solution:
    def knightDialer(self, N: int) -> int:
        # x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        # for i in range(N - 1):
        #     x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
        #         x6 + x8, x7 + x9, x4 + x8, \
        #         x3 + x9 + x0, 0, x1 + x7 + x0, \
        #         x2 + x6, x1 + x3, x2 + x4, \
        #         x4 + x6
        # return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)
        
        x = [1,1,1,1,1,1,1,1,1,1]
        for i in range(N-1):
            x = [x[4] + x[6],x[6] + x[8], x[7] + x[9], x[4] + x[8], \
                x[3] + x[9] + x[0], 0, x[1] + x[7] + x[0], \
                x[2] + x[6], x[1] + x[3], x[2] + x[4], \
                ]
        return sum(x)% (10**9 + 7)
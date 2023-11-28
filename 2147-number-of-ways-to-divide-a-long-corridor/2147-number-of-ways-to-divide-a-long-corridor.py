class Solution:
    def numberOfWays(self, corridor: str) -> int:
#         n = len(corridor)
#         ans = 0
#         mod = 10**9 +7
#         count = [[0,0] for _ in range(n+1)]
#         for i in range(0,n):
           
#             count[i+1] = copy.deepcopy(count[i])
#             if corridor[i] == 'P': count[i+1][0]+=1
#             if corridor[i] == 'S': count[i+1][1]+=1
#             print(count,"1")
#         if count[n][1] < 2:
#             return 0
#         if count[n][1] == 2:
#             return 1
            
#         for i in range(1,n):
#             l_pot,l_seat = count[i]
#             r_seat = count[n][1]-l_seat
#             print(i,l_seat,r_seat)
#             if l_seat ==2 and r_seat ==2:
#                 ans +=1
#         return ans%mod
        a, b, c = 1, 0, 0
        for ch in corridor:
            if ch == 'S':
                a, b, c = 0, a + c, b
            else:
                a, b, c = a + c, b, c
        return c % (10**9+7)
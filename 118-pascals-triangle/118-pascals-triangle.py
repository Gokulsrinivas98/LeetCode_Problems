class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = []
        for i in range(numRows):
            m = []
            for j in range(i+1):
                m.append(factorial(i)//(factorial(j)*factorial(i-j)))
            n.append(m)
        return n    
            
            
            
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
#  n!/(n-r)!r!
# for i in range(length):
#     for j in range(i+1):
#         n.append((factorial(i)//(factorial(j)*factorial(i-j)))
        
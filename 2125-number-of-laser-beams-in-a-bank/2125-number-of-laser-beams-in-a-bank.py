class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
#         m = len(bank)
#         if m == 1: return 0
#         ones = []
#         for i in range(m):
#             if bank[i].count('1') > 0:
#                 ones.append(bank[i].count('1'))

#         if len(ones) == 1: return 0 
        
#         for i in range(1,len(ones)):
#             res += ones[i]*ones[i-1]
            
#         return res
           
        m = len(bank)
        ones = [bank[i].count('1') for i in range(m) if '1' in bank[i]]
        if len(ones) == 1: return 0 
        return sum(ones[i] * ones[i-1] for i in range(1, len(ones)))    
        
       
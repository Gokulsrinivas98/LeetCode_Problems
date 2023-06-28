class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        if s[0] not in '-+0123456789 ' or "+-" in s or "-+" in s:
            return 0 
        
        numbers = ''.join((ch if ch in '-+0123456789' else ' ') for ch in s)
        numbers = numbers.strip().split(' ', 1)[0]
        print(numbers)
        if len(numbers) == 1 and numbers[0] in '-+ ':
            print(numbers)
            return 0
        if numbers and numbers[-1] in '-+':
            numbers = numbers[:-1]
        if '+' in numbers[1:]:
            numbers = numbers[:numbers.find('+', 1)]
        if '-' in numbers[1:]:
            numbers = numbers[:numbers.find('-', 1)]
        print(numbers)
        try:
            num = int(numbers)
        except ValueError:
            return 0
        if num> 2**31 - 1:
            return 2**31 - 1
        if num<-2**31:
            return -2**31
        return num
        
        
        
        
#         
#         if not s: return 0
#         
#         i = 0
#         while i < len(s) and s[i] == ' ':
#             i += 1
        
#         if i == len(s) or s[i] not in '+-0123456789':
#             return 0
#         numbers = ''.join((ch if ch in '-+0123456789' else ' ') for ch in s)
#         numbers = numbers.strip().split(' ', 1)[0]
#         print(numbers)
#         if len(numbers) == 1 and numbers[0] in '-+ ':
#             print(numbers)
#             return 0
#         if numbers and numbers[-1] in '-+':
#             numbers = numbers[:-1]
#         if '+' in numbers[1:]:
#             numbers = numbers[:numbers.find('+', 1)]
#         if '-' in numbers[1:]:
#             numbers = numbers[:numbers.find('-', 1)]
#         print(numbers)
#         try:
#             num = int(numbers)
#         except ValueError:
#             return 0
#         if num> 2**31 - 1:
#             return 2**31 - 1
#         if num<-2**31:
#             return -2**31
#         return num
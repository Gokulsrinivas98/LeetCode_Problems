# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         length = len(temperatures)
#         answer = [0]*length
#         stack = []
#         for i in range(length):
#             count = 0
#             while stack and temperatures[i] > temperatures[stack[-1]]:
#                 prev_day = stack.pop()
#                 answer[prev_day] = i- prev_day
#             stack.append(i)
#         return answer

f = open('user.out', 'w')
for temperatures in stdin:
    temperatures = loads(temperatures)

    res = [0] * len(temperatures)
    stack = []
    
    for day, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            top_index = stack.pop()
            res[top_index] = day - top_index

        stack.append(day)


    print("".join(['[', ','.join(str(x) for x in res), ']']), file=f)

exit(0)
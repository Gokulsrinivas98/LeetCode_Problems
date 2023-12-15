class Solution:
    def decodeString(self, s: str) -> str:
        stack , curr_num , curr_st = [],0,''
        for i in s:
            if i == '[':
                stack.append(curr_st)
                stack.append(curr_num)
                curr_num = 0
                curr_st = ''
            elif i == ']':
                num = stack.pop()
                prev_st = stack.pop()
                curr_st = prev_st + num * curr_st
            elif i.isdigit():
                curr_num = 10 * curr_num + int(i)
            else:
                curr_st += i
        return curr_st
class Solution:
    def minInsertions(self, s: str) -> int:
        # left = right = 0
        # for c in s:
        #     if c == '(':
        #         if right % 2:
        #             right -= 1
        #             left += 1
        #         right += 2
        #     if c == ')':
        #         right -= 1
        #         if right < 0 :
        #             right += 2
        #             left += 1 
        # return left + right
        
        s = s.replace('))', '}')
        miss_bracket = req_close = 0
        for c in s:
            if c == '(':
                req_close += 2
            else:
                if c == ')':
                    miss_bracket += 1
                if req_close:
                    req_close -= 2
                else:
                    miss_bracket += 1
        return req_close + miss_bracket
                    
        
class Solution:
    def isValid(self, s: str) -> bool:
        char = []
        for i in s:
            if i in ['(','[','{']:
                char.append(i)
            else:
                if not char:
                    return False
                if i == ')' and char[-1] =='(' or i == ']' and char[-1] =='[' or i == '}' and char[-1] =='{':
                    char.pop()
                else:
                    return False
        return not char
                    
        
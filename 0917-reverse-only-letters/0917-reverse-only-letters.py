class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start, end = 0, len(s)-1 
        s_list = list(s)
        while start < end:
            if s_list[start].isalpha() and s_list[end].isalpha():
                s_list[start],s_list[end] = s_list[end],s_list[start]
                start += 1
                end -=1
            elif not s_list[start].isalpha():
                start += 1
            elif not s_list[end].isalpha():
                end -= 1
        return "".join(s_list)
            
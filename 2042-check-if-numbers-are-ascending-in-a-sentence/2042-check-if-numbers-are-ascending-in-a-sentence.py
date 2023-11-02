class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # s_list = list(s.split())
        s_num = [int(i) for i in s.split() if i.isdigit()]
        return sorted(s_num) == s_num and len(s_num) == len(set(s_num))
        
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal:
            temp = set(s)
            return len(temp) < len(goal) 
        n_s,n_goal = '',''
        for s,g in zip(s,goal):
            if s!= g:
                n_s +=s
                n_goal +=g
        if len(n_s) != len(n_goal) or len(n_s) != 2 or len(n_s)==0: return False
        if n_s[0] != n_goal[1] or n_s[1] != n_goal[0] : return False
        else: return True
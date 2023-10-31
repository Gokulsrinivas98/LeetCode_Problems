class Solution:
    def totalMoney(self, n: int) -> int:
        week = [1,2,3,4,5,6,7]
        if n <= 7 : return sum(week[0:n])
        times = n // 7
        rem = n % 7
        s = 0
        while times > 0:
            s += sum(week)
            week = [i+1 for i in week]    
            times -= 1
        return s + sum(week[0:rem])
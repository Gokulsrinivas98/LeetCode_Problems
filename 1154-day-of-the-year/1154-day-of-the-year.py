class Solution:
    def dayOfYear(self, date: str) -> int:
        def is_leap_year(year):
              if year % 400 == 0:
                return True
              elif year % 100 == 0:
                return False
              elif year % 4 == 0:
                return True
              else:
                return False
        
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]
        
        dates = list(map(int,date.split('-')))
        print(dates)
        if is_leap_year(dates[0]):
            return sum(leap_days[0:dates[1]-1]) + dates[2]
        else:
            return sum(days[0:dates[1]-1]) + dates[2]
        
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        #flight is a boolean matrix of flights between cities i and j
        #flights[i][j] == 0 no flight between cities i and j
        #flights[i][j] == 1 if there are flight
        #flight[i][i] == 0 no flight to same country
        #so diagonal zero matrix
        #can fly only on mondaay mornings
        #days[i][j] reps max holidays in city i in week j
        k = len(days[0])
        vac = [[-1]*len(days) for i in range(k)]
        
        for week in range(k-1,-1,-1):
            for city in range(len(days)):
                if week == k-1:
                    vac[week][city] = max(days[dest][week] for dest in range (len(days)) if flights[city][dest] or dest == city)
                else: 
                    vac[week][city] = max(days[dest][week] + vac[week+1][dest] for dest in range(len(days)) if flights[city][dest] or dest==city)
        return vac[0][0]            
        
        

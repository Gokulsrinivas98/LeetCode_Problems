class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #capacity -> no of seats
        # trip[i] = [numPassengersi, fromi, toi]
        # m = max([trips[i][2] for i in range(len(trips))])
        arr = [0] * 1001
        for i in trips:
            for j in range(i[1],i[2],1):
                arr[j] += i[0]
                if arr[j] > capacity:
                    return False
        return True
        
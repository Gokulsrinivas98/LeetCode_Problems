class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == 1:
            return max(arr[0],arr[1])
        if k >= n:
            return max(arr)
        winner = arr[0]
        cons_wins = 0
        for i in range(1,n):
            if winner > arr[i]:
                cons_wins += 1
            else:
                winner = arr[i]
                cons_wins = 1
            
            if cons_wins == k:
                return winner
        return winner
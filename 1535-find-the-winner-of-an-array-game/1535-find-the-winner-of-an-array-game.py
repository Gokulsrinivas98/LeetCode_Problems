class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        winner = arr[0]
        cons_wins = 0
        for i in range(1,n):
            if winner < arr[i]:
                winner = arr[i]
                cons_wins = 1
            else:
                cons_wins += 1
            
            if cons_wins == k:
                return winner
        return winner
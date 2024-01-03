class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rad = deque()
        dir = deque()
        n = len(senate)
        # Add all senators to respect queue with index
        for i in range(n):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dir.append(i)
        # Use increasing n to keep track of position
        while rad and dir:
            # Only "winner" stays in their queue
            if rad[0] < dir[0]:
                rad.append(n)
            else:
                dir.append(n)
            n += 1
            rad.popleft()
            dir.popleft()
        return "Dire" if not rad else "Radiant"
        
       
from numpy import array
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = []
        for r in range(3):
            for c in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(board[3*r + i][3*c + j])
                answer.append(block)
        
        b2 =  list(map(list, zip(*board)))
        for i in range(9):
            if len([s for s in board[i] if s != '.']) != len(set(board[i]))-1  or len([s for s in b2[i] if s != '.']) != len(set(b2[i]))-1 or len([s for s in answer[i] if s != '.']) != len(set(answer[i]))-1:
                return False
                
        return True
                
        
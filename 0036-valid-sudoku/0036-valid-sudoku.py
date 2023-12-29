class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColumnValid(board) and self.isGridValid(board)
    
    def isRowValid(self, board):
        for i in board:
            if not self.listValid(i):
                print('row')
                return False
        return True
    
    def isColumnValid(self,board):
        for i in zip(*board):
            if not self.listValid(i):
                print('column')
                return False
        return True
    
    def isGridValid(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                llist  = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.listValid(llist):
                    print('grid')
                    return False
        return True
        
    
    def listValid(self, llist):
        l = [i for i in llist if i != '.']
        return len(set(l)) == len(l)
    
         
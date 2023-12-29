class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         return self.isRowValid(board) and self.isColumnValid(board) and self.isGridValid(board)
    
#     def isRowValid(self, board):
#         for i in board:
#             if not self.listValid(i):
#                 print('row')
#                 return False
#         return True
    
#     def isColumnValid(self,board):
#         for i in zip(*board):
#             if not self.listValid(i):
#                 print('column')
#                 return False
#         return True
    
#     def isGridValid(self,board):
#         for i in (0,3,6):
#             for j in (0,3,6):
#                 llist  = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
#                 if not self.listValid(llist):
#                     print('grid')
#                     return False
#         return True
        
    
#     def listValid(self, llist):
#         l = [i for i in llist if i != '.']
#         return len(set(l)) == len(l)
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isalnum():
                    k = i//3 * 3 + j//3
                    if val in row[i] or val in col[j] or val in grid[k]:
                        return False
                    else:
                        row[i].add(val)
                        col[j].add(val)
                        grid[k].add(val)

        return True    

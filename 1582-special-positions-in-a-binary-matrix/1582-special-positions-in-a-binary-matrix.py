class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def getColumnSum( mat, j):
            return sum([row[j] for row in mat])
    
    
        result = 0
        for row in mat:
            if sum(row) == 1:
                result += int(getColumnSum(mat, row.index(1)) == 1) 
        return result
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                
                k = i//3 * 3 + j//3
                if val in row[i] or val in col[j]:
                    return False
                else:
                    row[i].add(val)
                    col[j].add(val)
        return True
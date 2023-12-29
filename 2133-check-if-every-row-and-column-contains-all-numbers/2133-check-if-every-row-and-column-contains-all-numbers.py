class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = {i for i in range(1, len(matrix) + 1)}
        for row in matrix:
            if set(row) != check:
                return False
        for column in zip(*matrix):
            if set(column) != check:
                return False
        return True
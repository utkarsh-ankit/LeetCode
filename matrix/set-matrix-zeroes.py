class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # 1. Record all zero positions
        zeros = [(i, j)
                 for i in range(m)
                 for j in range(n)
                 if matrix[i][j] == 0]
        
        # 2. Zero out each recorded row and column
        for i, j in zeros:
            # zero entire row i
            for col in range(n):
                matrix[i][col] = 0
            # zero entire column j
            for row in range(m):
                matrix[row][j] = 0

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        rows_set = set()
        cols_set = set()
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    rows_set.add(row)
                    cols_set.add(col)
        for row in range(num_rows):
            for col in range(num_cols):
                if row in rows_set:
                    matrix[row][col] = 0
                elif col in cols_set:
                    matrix[row][col] = 0
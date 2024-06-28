class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
        # print(matrix)
        # print(first_col_has_zero, first_row_has_zero)
        for row in range(1,num_rows):
            for col in range(1,num_cols):
                matrix[row][col] = 0 if matrix[row][0] == 0 or matrix[0][col] == 0 else matrix[row][col]
        # print(matrix)   
        if first_row_has_zero:
            for col in range(num_cols):
                matrix[0][col] = 0
        if first_col_has_zero:
            for row in range(num_rows):
                matrix[row][0] = 0
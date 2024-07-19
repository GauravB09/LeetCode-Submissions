class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        MAX_NUM = 1000000
        MIN_NUM = 0
        min_in_rows = [MAX_NUM for _ in range(rows)]
        max_in_cols = [MIN_NUM for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] > max_in_cols[col]:
                    max_in_cols[col] = matrix[row][col]
                if matrix[row][col] < min_in_rows[row]:
                    min_in_rows[row] = matrix[row][col]
        set_of_min_in_rows = set(min_in_rows)
        set_of_max_in_cols = set(max_in_cols)
        return list(set_of_min_in_rows.intersection(set_of_max_in_cols))

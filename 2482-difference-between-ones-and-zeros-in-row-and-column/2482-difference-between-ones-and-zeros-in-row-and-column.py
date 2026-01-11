class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        rows_ones = [0] * rows
        cols_ones = [0] * cols
        rows_zeros = [0] * rows
        cols_zeros = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    rows_ones[i] += 1
                    cols_ones[j] += 1
                else:
                    rows_zeros[i] += 1
                    cols_zeros[j] += 1
        result = [[rows_ones[i] + cols_ones[j] - rows_zeros[i] - cols_zeros[j] for j in range(cols)] for i in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         result = rows_ones[i] + cols_ones[j] - rows_zeros[i] - cols_zeros[j]
        return result
        
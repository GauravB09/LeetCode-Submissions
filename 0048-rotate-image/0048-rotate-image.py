class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rows = n - 1
        for loop in range(n//2):
            for i in range(rows):
                matrix[loop][loop + i], matrix[n - i - loop - 1][loop] = matrix[n - i - loop - 1][loop], matrix[loop][loop + i]
                matrix[n - i - loop - 1][loop], matrix[n - loop - 1][n - i - loop - 1] = matrix[n - loop - 1][n - i - loop - 1], matrix[n - i - loop - 1][loop]
                matrix[n - loop - 1][n - i - loop - 1], matrix[loop + i][n - loop - 1] = matrix[loop + i][n - loop - 1], matrix[n - loop - 1][n - i - loop - 1]
            rows -= 2
        
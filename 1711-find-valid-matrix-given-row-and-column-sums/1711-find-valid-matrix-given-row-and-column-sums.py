class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # N = len(rowSum)
        # M = len(colSum)

        # curr_row_sum = [0] * N
        # curr_col_sum = [0] * M

        # orig_matrix = [[0] * M for _ in range(N)]
        # for i in range(N):
        #     for j in range(M):
        #         orig_matrix[i][j] = min(
        #             rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j]
        #         )

        #         curr_row_sum[i] += orig_matrix[i][j]
        #         curr_col_sum[j] += orig_matrix[i][j]

        # return orig_matrix
        
        # N = len(rowSum)
        # M = len(colSum)

        # orig_matrix = [[0] * M for _ in range(N)]
        # for i in range(N):
        #     for j in range(M):
        #         orig_matrix[i][j] = min(rowSum[i], colSum[j])

        #         rowSum[i] -= orig_matrix[i][j]
        #         colSum[j] -= orig_matrix[i][j]

        # return orig_matrix

        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return orig_matrix
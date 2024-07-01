class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        dic = {}
        for row in range(rows):
            for col in range(cols):
                count = 0
                if row-1 >= 0:
                    count += board[row-1][col]
                    if col-1 >= 0:
                        count += board[row-1][col-1]
                    if col+1 < cols:
                        count += board[row-1][col+1]
                if row+1 < rows:
                    count += board[row+1][col]
                    if col-1 >= 0:
                        count += board[row+1][col-1]
                    if col+1 < cols:
                        count += board[row+1][col+1]
                if col-1 >= 0:
                    count += board[row][col-1]
                if col+1 < cols:
                    count += board[row][col+1]
                # print(board[row][col], count)
                dic[(row, col)] = 1 if (board[row][col] == 0 and count == 3) else (0 if (board[row][col] == 1 and (count > 3 or count < 2)) else board[row][col])
        # print(dic)
        for row in range(rows):
            for col in range(cols):
                board[row][col] = dic[(row, col)]
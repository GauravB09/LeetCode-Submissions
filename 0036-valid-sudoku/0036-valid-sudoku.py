class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                # print(row, col, board[row][col], dic)
                if (('row_' + str(row)) in dic and board[row][col] in dic['row_' + str(row)]) or (('col_' + str(col)) in dic and board[row][col] in dic['col_' + str(col)]) or (('box_' + str(3 * (row//3) + col//3)) in dic and board[row][col] in dic['box_' + str(3 * (row//3) + col//3)]):
                    return False
                if ('row_' + str(row)) not in dic:
                    dic['row_' + str(row)] = set()
                if ('col_' + str(col)) not in dic:
                    dic['col_' + str(col)] = set()
                if ('box_' + str(3 * (row//3) + col//3)) not in dic:
                    dic['box_' + str(3 * (row//3) + col//3)] = set()
                dic['row_' + str(row)].add(board[row][col])
                dic['col_' + str(col)].add(board[row][col])
                dic['box_' + str(3 * (row//3) + col//3)].add(board[row][col])
        return True


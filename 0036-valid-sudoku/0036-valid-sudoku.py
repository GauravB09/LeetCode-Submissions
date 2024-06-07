class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                # print(row, col, board[row][col], dic)
                if (board[row][col] in rows[row]) or (board[row][col] in cols[col]) or  (board[row][col] in boxes[str(3 * (row//3) + col//3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[str(3 * (row//3) + col//3)].add(board[row][col])
        return True


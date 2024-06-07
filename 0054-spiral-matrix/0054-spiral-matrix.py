class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 1:
            return matrix[0]
        if cols == 1:
            return [matrix[i][0] for i in range(rows)]
        res_size = rows * cols
        res = [-10000 for i in range(res_size)]
        rows -= 1
        count = 0
        rev = False
        pos = [0, -1]
        while rows >= 0 and cols >= 0:
            # print(rows, cols)
            for _ in range(cols):
                if count >= res_size:
                    return res
                if not rev:
                    pos[1] += 1
                else:
                    pos[1] -= 1
                # print(pos, count)
                # print(res)
                res[count] = matrix[pos[0]][pos[1]]
                count += 1
            cols -= 1
            for _ in range(rows):
                if count >= res_size:
                    return res
                if not rev:
                    pos[0] += 1
                else:
                    pos[0] -= 1
                # print(pos, count)
                # print(res)
                res[count] = matrix[pos[0]][pos[1]]
                count += 1
            rows -= 1
            rev = rev ^ True
        return res

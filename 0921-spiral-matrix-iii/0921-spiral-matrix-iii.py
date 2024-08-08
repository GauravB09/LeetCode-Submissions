class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        count = 1
        total_count = rows * cols
        shift = 0
        go_right = True
        curr_pos = [rStart, cStart]
        ans = [[rStart, cStart]]
        while count < total_count:
            shift += 1
            if go_right:
                for i in range(shift):
                    curr_pos[1] += 1
                    # print('Right', curr_pos)
                    if curr_pos[0] < rows and curr_pos[1] < cols and curr_pos[0] >= 0 and curr_pos[1] >= 0:
                        ans.append([curr_pos[0], curr_pos[1]])
                        # print('Right', ans, count)
                        count += 1
                for i in range(shift):
                    curr_pos[0] += 1
                    # print('Down', curr_pos)
                    if curr_pos[0] < rows and curr_pos[1] < cols and curr_pos[0] >= 0 and curr_pos[1] >= 0:
                        ans.append([curr_pos[0], curr_pos[1]])
                        # print('Down', ans, count)
                        count += 1
                go_right = False
            else:
                for i in range(shift):
                    curr_pos[1] -= 1
                    # print('Left', curr_pos)
                    if curr_pos[0] < rows and curr_pos[1] < cols and curr_pos[0] >= 0 and curr_pos[1] >= 0:
                        ans.append([curr_pos[0], curr_pos[1]])
                        # print('Left', ans, count)
                        count += 1
                for i in range(shift):
                    curr_pos[0] -= 1
                    # print('Up', curr_pos)
                    if curr_pos[0] < rows and curr_pos[1] < cols and curr_pos[0] >= 0 and curr_pos[1] >= 0:
                        ans.append([curr_pos[0], curr_pos[1]])
                        # print('Up', ans, count)
                        count += 1
                go_right = True
        return ans



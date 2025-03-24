class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False if grid[i][j] == "1" else True for j in range(m)] for i in range(n)]
        def solve(visited, i, j, n, m):
            if i >=0 and j >= 0 and i < n and j < m and not visited[i][j]:
                visited[i][j] = True
                # print(visited, i, j)
                visited = solve(visited, i, j-1, n, m)
                visited = solve(visited, i, j+1, n, m)
                visited = solve(visited, i-1, j, n, m)
                visited = solve(visited, i+1, j, n, m)
            return visited
        
        answer = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    answer += 1
                    visited = solve(visited, i, j, n, m)
        return answer


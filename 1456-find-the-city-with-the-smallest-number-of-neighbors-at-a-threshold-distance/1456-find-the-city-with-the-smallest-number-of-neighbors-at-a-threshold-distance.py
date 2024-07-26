class Solution:
    def floydWarshall(self, graph: List[List[int]], n: int) -> List[List[int]]:
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 100000000
        graph = [[INF for _ in range(n)] for __ in range(n)]
        for edge in edges:
            start, end, weight = edge
            graph[start][end] = weight
            graph[end][start] = weight
        for i in range(n):
            graph[i][i] = 0
        distance_graph = self.floydWarshall(graph, n)
        min_cities_reached = 10000000
        ans = -1
        for i in range(n):
            cities_reached = 0
            for j in range(n):
                if distance_graph[i][j] <= distanceThreshold:
                    cities_reached += 1
            if cities_reached < min_cities_reached:
                min_cities_reached = cities_reached
                ans = i
            elif cities_reached == min_cities_reached:
                ans = i
        return ans
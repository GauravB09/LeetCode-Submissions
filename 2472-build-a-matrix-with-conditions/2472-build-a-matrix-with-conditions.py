class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def get_indices(conditions, arr):
            indegree = [0] * (k + 1)
            graph = defaultdict(list)

            for u, v in conditions:
                indegree[v] += 1
                graph[u].append(v)
            
            queue = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)
            
            i = 0
            while queue: 
                u = queue.popleft()
                arr[u] = i
                i += 1
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            if i != k:
                return []
            return arr
    
        rows = get_indices(rowConditions, [0] * (k + 1))
        cols = get_indices(colConditions, [0] * (k + 1))

        if not rows or not cols:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            matrix[rows[i]][cols[i]] = i
        return matrix
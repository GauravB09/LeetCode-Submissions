class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {}
        for i in range(n):
            graph[i] = []
        count = [0 for i in range(n)]
        visited = [False for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            count[edge[1]] += 1
        topo_sorted = []
        # print(graph)
        # print(count, visited)
        while not all(visited):
            # print(count, visited)
            for i in range(n):
                if count[i] == 0 and not visited[i]:
                    visited[i] = True
                    topo_sorted.append(i)
                    for j in graph[i]:
                        count[j] -= 1
        # print(topo_sorted)
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]
        for node in topo_sorted:
            for neighbor in graph[node]:
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])
        for i in range(n):
            ancestors_list[i].extend(ancestors_set_list[i])
            ancestors_list[i].sort()

        return ancestors_list

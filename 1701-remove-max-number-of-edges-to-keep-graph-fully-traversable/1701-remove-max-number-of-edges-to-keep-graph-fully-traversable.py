# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # alice_edges = {}
        # bob_edges = {}
        # common_count = 0
        # alice_count = 0
        # bob_count = 0
        # for i in range(1,n+1):
        #     alice_edges[i] = []
        #     bob_edges[i] = []
        # for edge in edges:
        #     if edge[0] == 3:
        #         alice_edges[edge[1]].append(edge[2])
        #         alice_edges[edge[2]].append(edge[1])
        #         bob_edges[edge[1]].append(edge[2])
        #         bob_edges[edge[2]].append(edge[1])
        #         common_count += 1
        #     elif edge[0] == 1:
        #         alice_edges[edge[1]].append(edge[2])
        #         alice_edges[edge[2]].append(edge[1])
        #         alice_count += 1
        #     else:
        #         bob_edges[edge[1]].append(edge[2])
        #         bob_edges[edge[2]].append(edge[1])
        #         bob_count += 1
        # visited_alice = [False for _ in range(n)]
        # queue = [1]
        # while queue:
        #     elem = queue.pop(0)
        #     if not visited_alice[elem-1]:
        #         visited_alice[elem-1] = True
        #         queue += alice_edges[elem]
        # visited_bob = [False for _ in range(n)]
        # queue = [1]
        # while queue:
        #     elem = queue.pop(0)
        #     if not visited_bob[elem-1]:
        #         visited_bob[elem-1] = True
        #         queue += bob_edges[elem]
        # if not (all(visited_alice) and all(visited_bob)):
        #     return -1
        # print(alice_count, bob_count, common_count)
        # return (alice_count + bob_count + common_count - (n-1)) if common_count >= (n-1) else (alice_count - ((n-1) - common_count) + bob_count - ((n-1) - common_count))

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        auf = UnionFind(n)
        buf = UnionFind(n)
        res = 0
        for edge in edges:
            if edge[0] == 3:
                if auf.union(edge[1], edge[2]) == 1:
                    buf.union(edge[1], edge[2])
                    res += 1
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        for edge in edges:
            if edge[0] == 1:
                res += auf.union(edge[1], edge[2])
            if edge[0] == 2:
                res += buf.union(edge[1], edge[2])
            if auf.is_connected() and buf.is_connected():
                return len(edges) - res
        return -1

class UnionFind:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.node_count = n
    def find(self, x):
        if self.parent[x] == 0 or self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 0
        self.parent[py] = px
        self.node_count -= 1
        return 1
    def is_connected(self):
        return self.node_count == 1

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0 for _ in range(n)]
        for node_1, node_2 in roads:
            arr[node_1] += 1
            arr[node_2] += 1
        arr.sort(reverse=True)
        count = n
        ans = 0
        for i in range(n):
            ans += arr[i] * count
            count -= 1
        return ans
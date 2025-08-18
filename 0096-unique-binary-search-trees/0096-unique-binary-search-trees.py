class Solution:
    def numTrees(self, n: int) -> int:
        arr = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            total = 0
            for root in range(1, i + 1):
                total += arr[root-1] * arr[i - root]
            arr[i] = total
        return arr[n]

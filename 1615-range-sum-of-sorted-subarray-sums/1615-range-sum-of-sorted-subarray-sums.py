class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = (10 ** 9) + 7
        prefix_sum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        arr = [0 for _ in range((n * (n + 1)) // 2)]
        i = 0
        for start in range(n):
            for end in range(start + 1, n + 1):
                arr[i] = prefix_sum[end] - prefix_sum[start]
                i += 1
        arr.sort()
        ans = 0
        for i in range(left-1, right):
            ans += arr[i]
        return ans % MOD
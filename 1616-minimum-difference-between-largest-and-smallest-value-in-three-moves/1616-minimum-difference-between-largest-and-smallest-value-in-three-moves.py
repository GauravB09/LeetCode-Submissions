class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        ans = 10 ** 10
        for i in range(4):
            ans = min(nums[n - 4 + i] - nums[i], ans)
        return ans

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n <= 4:
        #     return 0
        # nums.sort()
        # ans = 10 ** 10
        # for i in range(4):
        #     ans = min(nums[n - 4 + i] - nums[i], ans)
        # return ans
        nums_size = len(nums)
        if nums_size <= 4:
            return 0
        smallest_four = sorted(heapq.nsmallest(4, nums))
        largest_four = sorted(heapq.nlargest(4, nums))
        min_diff = float("inf")
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])
        return min_diff

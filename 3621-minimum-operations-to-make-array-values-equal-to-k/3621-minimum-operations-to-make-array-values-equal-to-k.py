class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        ans = 0
        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            if nums[i] not in s and nums[i] > k:
                ans += 1
                s.add(nums[i])
        return ans
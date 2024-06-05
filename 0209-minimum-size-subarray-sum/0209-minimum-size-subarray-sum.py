class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        if n == 1:
            return int(nums[0] >= target)
        ans = 100001
        current_sum = nums[0]
        while j < n:
            if i == j:
                break
            if current_sum < target:
                current_sum += nums[j]
                j += 1
            else:
                ans = min(ans, j-i)
                current_sum -= nums[i]
                i += 1
        while current_sum >= target:
            ans = min(ans, j-i)
            current_sum -= nums[i]
            i += 1
            if i == j:
                break
        if ans == 100001:
            return 0
        return ans 
            
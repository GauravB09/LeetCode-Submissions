class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0 
        reachable = 0
        current_end = 0
        n = len(nums)
        for i in range(n-1):
            reachable = max(reachable, i + nums[i])
            if i == current_end:
                result += 1
                current_end = reachable
        return result
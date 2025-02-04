class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = len(nums)
        result = nums[0]
        temp = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                result = max(result, temp)
                temp = nums[i]
        return max(result, temp)
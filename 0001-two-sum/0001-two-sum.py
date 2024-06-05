class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            if (target-nums[i]) in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i

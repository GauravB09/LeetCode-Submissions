class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        miss = 1
        index = 0
        length = len(nums)
        while miss <= n:
            if index < length and miss >= nums[index]:
                miss += nums[index]
                index += 1
            else:
                miss *= 2
                result += 1
        return result
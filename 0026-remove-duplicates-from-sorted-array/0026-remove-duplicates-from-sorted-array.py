class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = -101
        index = 0
        pos = 0
        n = len(nums)
        while index != n:
            if nums[index] != temp:
                nums[index], nums[pos] = nums[pos], nums[index]
                temp = nums[pos]
                pos += 1
            index += 1
        return pos
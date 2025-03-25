class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        count = 0
        j = 0
        while i < n:
            if nums[i] == 0:
                count += 1
            else:
                nums[j] = nums[i]
                j += 1
            i += 1
        for i in range(count):
            nums[n-i-1] = 0
        return nums
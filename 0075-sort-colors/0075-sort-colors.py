class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = 0
        w = 0
        b = n-1
        while w <= b:
            # print(nums)
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                if w < r:
                    w = r
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:
                w += 1
        return nums
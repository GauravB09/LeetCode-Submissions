class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = True
        pos = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[pos-1]:
                check = True
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            elif check:
                check = False
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return pos
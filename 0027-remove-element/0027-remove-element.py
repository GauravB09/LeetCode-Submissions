class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
            elif nums[start] == val:
                nums[start] = nums[end]
                nums[end] = val
                start += 1
            else: 
                start += 1
        return start
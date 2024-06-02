class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        n = len(nums)
        elem = nums[0]
        for i in range(1,n):
            if cnt == 0:
                elem = nums[i]
            if nums[i] == elem:
                cnt += 1
            else:
                cnt -= 1
        return elem
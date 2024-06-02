class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for i in dic:
            if dic[i] > n//2:
                return i
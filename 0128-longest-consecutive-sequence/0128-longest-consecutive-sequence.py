class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        n = len(nums)
        ans = 0
        temp = 1
        for i in range(1,n):
            if nums[i-1] == nums[i]:
                continue
            # print(nums[i-1], nums[i], temp, ans)
            if nums[i-1]+1 != nums[i]:
                ans = max(ans, temp)
                temp = 0
            temp += 1
        return max(ans, temp)
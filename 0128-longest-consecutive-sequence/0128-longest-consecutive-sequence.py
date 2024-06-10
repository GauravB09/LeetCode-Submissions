class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num - 1 not in s:
                temp = 1
                while num + temp in s:
                    temp += 1
                ans = max(ans, temp)
        return ans
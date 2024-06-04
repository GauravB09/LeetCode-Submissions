class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        prev_i = -1000001
        for i in range(n):
            if nums[i] != prev_i:
                prev_i = nums[i]
                j = i + 1
                k = n - 1
                prev_j = -1000001
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0 and nums[j] != prev_j:
                        res.append([nums[i], nums[j], nums[k]])
                        prev_j = nums[j]
                        k -= 1
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1
        return res
        

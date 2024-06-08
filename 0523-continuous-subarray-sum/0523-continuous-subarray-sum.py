class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        n = len(nums)
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            rem = curr_sum % k
            if rem in dic:
                if i - dic[rem] > 1:
                    return True
            else:
                dic[rem] = i
        return False
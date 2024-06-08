class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {}
        n = len(nums)
        for i in range(n):
            if i<n-1 and ((nums[i] == 0 and nums[i+1] == 0) or (nums[i] == 0 and nums[i+1]%k == 0) or (nums[i]%k == 0 and nums[i+1] == 0)):
                return True
            nums[i] = nums[i]%k
        # print(nums)
        curr_sum = nums[0]
        last_index_before_zero = 0
        less_than_k = True
        # print(curr_sum)
        for i in range(1,n):
            if nums[i] != 0 :
                last_index_before_zero = i
            new_sum = curr_sum + nums[i]
            if new_sum >= k:
                less_than_k = False
            curr_sum = new_sum%k
            # print(curr_sum, new_sum, dic, less_than_k, last_index_before_zero)
            if curr_sum == 0 or (curr_sum in dic and not less_than_k and dic[curr_sum] < last_index_before_zero) or (i > 1 and curr_sum - nums[0] == 0):
                return True
            if curr_sum not in dic:
                dic[curr_sum] = i
        #     print(curr_sum, dic)
        # print(curr_sum, new_sum, dic, less_than_k, last_index_before_zero)
        return False
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # arr = []
        # count = 1
        # length = 0
        # for i in range(n):
        #     if nums[i] % 2 == 1:
        #         arr.append(count)
        #         count = 1
        #         length += 1
        #     count += 1
        # if nums[-1] % 2 != 1:
        #     arr.append(count-1)
        #     length += 1
        # print(arr)
        # ans = 0
        # for i in range(length - k):
        #     if i==0:
        #         a = arr[i]
        #     else:
        #         a = arr[i] - 1
        #     if i+k == length-1:
        #         b = arr[i+k]
        #     else:
        #         b = arr[i+k] - 1
        #     ans += a * b
        # return ans
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return subarrays
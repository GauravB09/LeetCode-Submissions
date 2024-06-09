class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum = (curr_sum + num)%k
            if curr_sum == 0:
                count += 1
            if curr_sum in dic:
                count += dic[curr_sum]
            else:
                dic[curr_sum] = 0
            dic[curr_sum] += 1
        return count

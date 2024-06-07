class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1 or k == 0:
            return False
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = i
            elif abs(dic[nums[i]] - i) <= k:
                return True
            else:
                dic[nums[i]] = i
        return False
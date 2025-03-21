class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_1 = [[nums[i], i] for i in range(n)]
        nums_1.sort()

        def bin_search(remainder, left, right):
            if left <= right:
                mid = (left + right)//2
                if nums_1[mid][0] == remainder:
                    return nums_1[mid][1]
                elif nums_1[mid][0] < remainder:
                    return bin_search(remainder, mid+1, right)
                else:
                    return bin_search(remainder, left, mid-1)
            return -1
        
        for i in range(n):
            remainder_index = bin_search(target-nums_1[i][0], i+1, n-1)
            if remainder_index != -1:
                return [nums_1[i][1],remainder_index]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for i in range(n)]
        res[0] = 1
        for i in range(1,n):
            res[i] = nums[i-1]*res[i-1]
        postfix_product = 1
        for i in range(n-2, -1 , -1):
            postfix_product *= nums[i+1]
            res[i] *= postfix_product
        return res
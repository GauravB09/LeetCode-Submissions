class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        nums = nums + [(-1) * ((2 ** 31) + 1)]
        n = len(nums)
        start = nums[0]
        for i in range(n-1):
            if nums[i]+1 != nums[i+1]:
                if start != nums[i]:
                    res.append(str(start) + "->" + str(nums[i]))
                else:
                    res.append(str(start))
                start = nums[i+1]
        # print(res)
        return res

            

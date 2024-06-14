class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        max_num = max(nums) + 1
        arr = [0 for _ in range(max_num)]
        for num in nums:
            arr[num] += 1
        s = []
        length = 0
        # print(arr)
        for i in range(max_num ):
            # print(s, arr[i], length)
            if arr[i] == 0 and length > 0:
                ans += i - s.pop()
                length -= 1
            elif arr[i] > 1:
                s = [i for _ in range(arr[i] - 1)] + s
                length += (arr[i] - 1)
        # print(s)
        for i in s:
            ans += max_num - i
            max_num += 1
        return ans
            

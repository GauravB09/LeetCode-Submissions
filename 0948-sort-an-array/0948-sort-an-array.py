import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        n = len(nums)
        arr = [heapq.heappop(nums) for _ in range(n)]
        return arr
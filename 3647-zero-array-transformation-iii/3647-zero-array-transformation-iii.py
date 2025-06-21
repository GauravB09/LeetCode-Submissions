import heapq
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        len_nums = len(nums)
        len_q = len(queries)
        heap = []
        queries.sort()
        diff_arr = [0 for _ in range(len_nums+1)]
        operations = 0
        idx = 0
        for i, num in enumerate(nums):
            operations += diff_arr[i]
            while idx < len_q and queries[idx][0] == i:
                heapq.heappush(heap, -queries[idx][1])
                idx += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                diff_arr[-heapq.heappop(heap)+1] -= 1
            if operations < num:
                return -1
        return len(heap)
            



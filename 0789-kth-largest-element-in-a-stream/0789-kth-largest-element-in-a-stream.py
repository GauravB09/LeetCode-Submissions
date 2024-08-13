class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.stream = nums
    #     self.stream.sort()

    # def add(self, val: int) -> int:
    #     index = self.getIndex(val)
    #     # Add val to correct position
    #     self.stream.insert(index, val)
    #     return self.stream[-self.k]

    # def getIndex(self, val: int) -> int:
    #     left, right = 0, len(self.stream) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         mid_element = self.stream[mid]
    #         if mid_element == val:
    #             return mid
    #         # Go to left half
    #         elif mid_element > val:
    #             right = mid - 1
    #         # Go to right half
    #         else:
    #             left = mid + 1
    #     return left

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to our min_heap if we haven't processed k elements yet
        # or if val is greater than the top element (the k-th largest)
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
class Solution:
    def searchIndexForDifficultyLessThanK(self, arr: List[List[int]], k: int, min: int, max: int) -> int:
        while min < max:
            mid = (max + min) // 2
            if arr[mid][0] < k + 1:
                min = mid + 1
            else:
                max = mid
        return min - 1

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        arr = [[0, 0]] + [[difficulty[i], profit[i]] for i in range(n)]
        arr.sort()
        temp = 0
        for i in range(n + 1):
            temp = max(temp, arr[i][1])
            arr[i][1] = temp
        result = 0
        print(arr)
        for i in worker:
            index = self.searchIndexForDifficultyLessThanK(arr, i, 0, n + 1)
            print(f"Index : {index}")
            result += arr[index][1]
        return result

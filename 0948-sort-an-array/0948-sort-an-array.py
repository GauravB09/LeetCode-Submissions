class Solution:
    def merge(self, arr1: List[int], arr2: List[int], n1: int, n2: int) -> List[int]:
        ans = [0 for _ in range(n1 + n2)]
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                ans[k] = arr1[i]
                i += 1
            else:
                ans[k] = arr2[j]
                j += 1
            k += 1
        while i < n1:
            ans[k] = arr1[i]
            i += 1
            k += 1
        while j < n2:
            ans[k] = arr2[j]
            j += 1
            k += 1
        return ans

    def mergeSort(self, arr: List[int], n: int) -> List[int]:
        if n == 1:
            return arr
        elif n == 2:
            return [arr[0], arr[1]] if arr[0] <= arr[1] else [arr[1], arr[0]]
        else:
            mid = n // 2
            arr1 = self.mergeSort(arr[:mid], mid)
            arr2 = self.mergeSort(arr[mid:], n - mid)
            return self.merge(arr1, arr2, mid, n - mid)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, len(nums))
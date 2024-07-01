class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        count = 0
        i = 0
        while i < n:
            if arr[i] % 2 == 0:
                count = 0
            else:
                count += 1
            if count == 3:
                return True
            i += 1
        return False

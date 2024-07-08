class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        count = n
        while count > 1:
            for i in range(k-1):
                arr.append(arr.pop(0))
            arr.pop(0)
            count -= 1
        return arr[0]
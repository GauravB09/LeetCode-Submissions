class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        arr = [i for i in range(2,n+1)]
        arr += [n - i for i in range(1,n)]
        # print(arr, (time % (2 * n)) - 1)
        return arr[(time % (2 * (n - 1))) - 1]
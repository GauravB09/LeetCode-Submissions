class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return 1 + time % (n - 1) if (time // (n - 1)) % 2 == 0 else n - (time % (n - 1))
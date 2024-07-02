class Solution:
    def trailingZeroes(self, n: int) -> int:
        return (n // (5 ** 1)) + (n // (5 ** 2)) + (n // (5 ** 3)) + (n // (5 ** 4)) + (n // (5 ** 5))
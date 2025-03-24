class Solution:
    def reverse(self, x: int) -> int:
        limit = (2 << 30)
        n = abs(x)
        res = 0
        while n > 0:
            # print(limit, 2 << 31, res, x)
            if (res > limit - 1 and x > 0) or (res > limit and x < 0):
                return 0
            res = (res * 10) + n % 10
            n = n // 10
        return 0 if (res > limit - 1 and x > 0) or (res > limit and x < 0) else res if x > 0 else -1 * res
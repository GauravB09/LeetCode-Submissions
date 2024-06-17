class Solution:
    def isSquare(self, n: int) -> bool:
        if n <= 1:
            return True
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == n:
                return True
            elif square < n:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        if self.isSquare(c):
            return True
        temp = 1
        num = 0
        while num <= c:
            num = temp * temp
            temp += 1
            if c - num >= 0 and self.isSquare(c - num):
                return True
        return False
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            square = mid ** 2
            if square == x :
                return mid
            elif square > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
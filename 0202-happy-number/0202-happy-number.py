class Solution:
    def getSumOfSquaresOfDigits(self, n):
        sum_of_squares_of_digits = 0
        while n > 0:
            sum_of_squares_of_digits += (n%10) ** 2
            n = n//10
        return sum_of_squares_of_digits

    def isHappy(self, n: int) -> bool:
        dic = set()
        if n == 1:
            return True
        while True:
            n = self.getSumOfSquaresOfDigits(n)
            if n == 1:
                return True
            if n in dic:
                return False
            dic.add(n)
            
class Solution:
    def getDigits(self, n):
        l = []
        while n > 0:
            l.append(n%10)
            n = n//10
        return tuple(sorted(l))

    def isHappy(self, n: int) -> bool:
        dic = set()
        if n == 1:
            return True
        while True:
            digits = self.getDigits(n)
            print(digits)
            if digits in dic:
                return False
            sum_of_squares_of_digits = 0
            for i in digits:
                sum_of_squares_of_digits += i*i
            if sum_of_squares_of_digits == 1:
                return True
            dic.add(digits)
            n = sum_of_squares_of_digits
            
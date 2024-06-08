class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 1:
            if digits[0] == 9:
                return [1, 0]
            return [digits[0]+1]
        for i in range(n-1, -1, -1):
            if digits[i]!=9:
                digits[i] += 1
                break
            digits[i] = 0
        if i == 0 and digits[0] == 0:
            return [1] + digits
        return digits
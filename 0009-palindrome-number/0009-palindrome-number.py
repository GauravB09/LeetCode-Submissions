class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new = 0
        prev = x
        while x > 0:
            new = (new*10) + x%10
            x = x // 10
        # print(x, new)
        return prev == new

            
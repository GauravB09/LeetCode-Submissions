class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        res = [0]
        temp = 1
        num = 0
        while num <= c:
            num = temp * temp
            temp += 1
            res.append(num)
        s = set(res)
        for i in res:
            if c - i in s:
                return True
        return False
class Solution:
    def decodeString(self, s: str) -> str:
        number = 0
        stack = []
        res = ''
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(number)
                res = ''
                number = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                res = prevString + res*num
            elif c.isdigit():
                number = number * 10 + int(c)
            else:
                res += c
        return res
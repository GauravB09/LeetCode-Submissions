class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        if x >= y:
            start_char, end_char = 'a', 'b'
        else:
            start_char, end_char = 'b', 'a'
        ans = 0
        for i in s:
            if i == end_char:
                if stack and stack[-1] == start_char:
                    ans += max(x, y)
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        temp = ''.join(stack)
        start_char, end_char = end_char, start_char
        stack = []
        for i in temp:
            if i == end_char:
                if stack and stack[-1] == start_char:
                    ans += min(x, y)
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return ans

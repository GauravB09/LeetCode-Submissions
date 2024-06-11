class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                s.append(- s.pop() + s.pop())
            elif i == '*':
                s.append(s.pop() * s.pop())
            elif i == '/':
                a = s.pop()
                b = s.pop()
                if a * b < 0:
                    s.append(-1 * (abs(b) // abs(a)))
                else:
                    s.append(abs(b) // abs(a))
            else:
                s.append(int(i))
        return s[0]
            
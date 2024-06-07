class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i not in pairs:
                stack.append(i)
            elif stack == []:
                return False
            elif stack[-1] == pairs[i]:
                stack.pop()
            else:
                return False
        return stack == []
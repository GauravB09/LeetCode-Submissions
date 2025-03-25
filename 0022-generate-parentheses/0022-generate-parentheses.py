class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateValidParentheses(result, s, left, right):
            if left > right:
                return result
            if left == 0:
                result.append(s + (")" * right))
                return result
            if left == right:
                result = generateValidParentheses(result, s + "(", left - 1, right)
            else:
                result = generateValidParentheses(result, s + "(", left - 1, right)
                result = generateValidParentheses(result, s + ")", left, right - 1)
            return result
        
        return generateValidParentheses([], "", n, n)
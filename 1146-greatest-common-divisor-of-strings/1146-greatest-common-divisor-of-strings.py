class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        for i in range(min(n1,n2), 0, -1):
            if str1[:i] * (n1//i) == str1 and str2[:i] * (n2//i) == str2 and str1[:i] == str2[:i]:
                return str1[:i]
        return ""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        s = ""
        for i in range(max(n1, n2)):
            if i < n1:
                s += word1[i]
            if i < n2:
                s += word2[i]
        return s
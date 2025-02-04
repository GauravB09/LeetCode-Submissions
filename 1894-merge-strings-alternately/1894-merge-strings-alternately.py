class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        s = ""
        for i in range(min(n1, n2)):
            s += word1[i]
            s += word2[i]
        s += word1[i+1:]
        s += word2[i+1:]
        return s
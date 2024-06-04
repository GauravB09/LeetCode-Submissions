class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0 for i in range(26)]
        len_s = len(s)
        if len(s)!=len(t):
            return False
        for i in range(len_s):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if alpha[i] != 0:
                return False
        return True

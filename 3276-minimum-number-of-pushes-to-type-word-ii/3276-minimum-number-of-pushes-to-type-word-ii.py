class Solution:
    def minimumPushes(self, word: str) -> int:
        alpha = [0 for  _ in range(26)]
        for char in word:
            alpha[ord(char) - ord('a')] += 1
        alpha.sort(reverse=True)
        ans = 0
        for i in range(26):
            ans += alpha[i] * ((i//8) + 1)
        return ans
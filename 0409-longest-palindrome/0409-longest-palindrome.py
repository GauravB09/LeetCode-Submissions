class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        ans = 0
        for i in s:
            if i not in chars:
                chars.add(i)
            else:
                chars.remove(i)
                ans += 2
        if bool(chars):
            return ans + 1
        return ans
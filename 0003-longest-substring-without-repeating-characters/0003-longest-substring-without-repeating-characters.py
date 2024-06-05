class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1
        n = len(s)
        if n <= 1:
            return n
        i = 0
        j = 0
        alpha = [-1 for i in range(1000)]
        while j < n:
            # print(i, j, alpha[ord(s[j])], s[i:j])
            if alpha[ord(s[j])]!=-1 and alpha[ord(s[j])] >= i:
                ans = max(ans, j-i)
                i = alpha[ord(s[j])]+1
            alpha[ord(s[j])] = j
            j+=1
        # print(i, j, s[i:j])
        return max(ans, j-i)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = strs[0]
        t = len(strs[0])
        n = len(strs)
        for i in range(1,n):
            j = 0
            t = min(t, len(strs[i]), len(s))
            while (j < t) and (strs[i][j] == s[j]):
                j+=1
            s = s[:j]
        return s
        
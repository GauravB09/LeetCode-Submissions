class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        ans = -1
        for i in range(len_h):
            if haystack[i] == needle[0]:
                if haystack[i:i+len_n] == needle:
                    return i
        return ans

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        j = 0
        len_s = len(s)
        len_t = len(t)
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                j+=1
            i+=1
        return len_t - j
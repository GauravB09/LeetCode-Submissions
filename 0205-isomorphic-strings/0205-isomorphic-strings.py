class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s!=len_t:
            return False
        dic_s = {}
        dic_t = {}
        ans = True
        for i in range(len_s):
            if t[i] not in dic_t:
                dic_t[t[i]] = s[i]
            elif s[i] != dic_t[t[i]]:
                ans = False
            if s[i] not in dic_s:
                dic_s[s[i]] = t[i]
            elif t[i] != dic_s[s[i]]:
                ans = False
        return ans
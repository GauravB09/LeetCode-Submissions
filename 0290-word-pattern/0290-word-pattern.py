class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        len_p = len(pattern)
        len_s = len(s)
        if len_p != len_s:
            return False
        dic = {}
        print(s, pattern)
        for i in range(len_p):
            print(dic)
            if pattern[i] not in dic:
                dic[pattern[i]] = s[i]
            if ("word" + s[i]) not in dic:
                dic[("word" + s[i])] = pattern[i]
            if dic[pattern[i]] != s[i] or dic[("word" + s[i])] != pattern[i]:
                return False
        return True
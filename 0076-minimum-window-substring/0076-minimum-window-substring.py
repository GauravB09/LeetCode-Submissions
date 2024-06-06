class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            return ""
        dic_t = [0 for _ in range(128)]
        start = 0
        end = 0
        sub_str_len = 10000001
        count = len_t
        temp = 0
        for i in range(count):
            dic_t[ord(t[i])] += 1
        while end < len_s:
            if dic_t[ord(s[end])] > 0:
                count -= 1
            dic_t[ord(s[end])] -= 1
            end += 1
            while count == 0:
                if end - start < sub_str_len:
                    temp = start
                    sub_str_len = end - start
                if dic_t[ord(s[start])] == 0:
                    count += 1
                dic_t[ord(s[start])] += 1
                start += 1
        if sub_str_len == 10000001:
            return ""
        return s[temp:temp+sub_str_len]
        
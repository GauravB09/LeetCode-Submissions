class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        arr_len = len(words)
        str_len = len(s)
        word_len = len(words[0])
        substr_len = word_len * arr_len
        if str_len < substr_len:
            return []
        # print(arr_len, str_len, word_len, substr_len)
        dic = {}
        for i in range(arr_len):
            if words[i] not in dic:
                dic[words[i]] = 0
            dic[words[i]] += 1
        # print(dic)
        res = []
        for j in range(word_len):
            # print(j, str_len - substr_len - word_len + 1)
            dic1 = {}
            for k in range(j, j + substr_len, word_len):
                word = s[k:k+word_len]
                # print(word)
                if word not in dic1:
                    dic1[word] = 0
                dic1[word] += 1
            if dic == dic1:
                res.append(j)
            # print(dic1, res)
            for i in range(j, str_len - substr_len - word_len + 1, word_len):
                word_removed = s[i:i+word_len]
                word_added = s[i+substr_len:i+substr_len+word_len]
                # print(word_removed, word_added)
                if word_removed in dic1:
                    if dic1[word_removed] == 1:
                        dic1.pop(word_removed)
                    else:
                        dic1[word_removed] -= 1
                else:
                    break
                if word_added not in dic1:
                    dic1[word_added] = 0
                dic1[word_added] += 1
                # print(dic1)
                if dic == dic1:
                    res.append(i+word_len)
        return res
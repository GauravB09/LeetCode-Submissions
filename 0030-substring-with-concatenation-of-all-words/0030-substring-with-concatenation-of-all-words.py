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
        for i in range(str_len - substr_len+1):
            dic1 = {}
            for j in range(i, i + substr_len, word_len):
                word = s[j:j+word_len]
                # print(word)
                if word not in dic:
                    break
                if word not in dic1:
                    dic1[word] = 0
                dic1[word] += 1
            # print(dic1)
            if dic == dic1:
                res.append(i)
        return res
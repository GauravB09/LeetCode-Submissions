class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = sentence.split()
        len_s = len(s)
        for i in dictionary:
            len_word = len(i)
            for j in range(len_s):
                if s[j][:len_word] == i:
                    s[j] = i
        return " ".join(s)
        
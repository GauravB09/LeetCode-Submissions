class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        max_int = (10 ** 9)+ 1
        arr = [max_int for _ in range(26)]
        n = 0
        for word in words:
            arr_temp = [0 for _ in range(26)]
            for char in word:
                arr_temp[ord(char) - ord('a')] += 1
            for index in range(26):
                arr[index] = min(arr[index], arr_temp[index])
        res = []
        for index in range(26):
            res += [chr(index + ord('a'))] * arr[index]
        return res
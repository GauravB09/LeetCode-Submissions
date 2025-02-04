class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        start = 0
        end = n - 1
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        while start < end:
            while start < n and s[start] not in vowels:
                start += 1
            while start < end and end >= 0 and s[end] not in vowels:
                end -= 1
            if start < end:
                s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)
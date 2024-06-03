class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_a = {}
        for i in magazine:
            if i not in dict_a:
                dict_a[i] = 0
            dict_a[i] += 1
        for i in ransomNote:
            if i not in dict_a:
                return False
            dict_a[i] -= 1
            if dict_a[i] < 0:
                return False
        return True
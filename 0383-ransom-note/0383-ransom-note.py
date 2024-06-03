class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0 for i in range(26)]
        for i in magazine:
            arr[ord(i)-ord('a')] += 1
        for i in ransomNote:
            val = ord(i)-ord('a')
            arr[val] -= 1
            if arr[val] < 0:
                return False
        return True
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for string in arr:
            if string not in dic:
                dic[string] = 0
            dic[string] += 1
        for string in arr:
            if dic[string] == 1:
                if k == 1:
                    return string
                k -= 1
        return ""
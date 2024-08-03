from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic = Counter(target)
        for i in arr:
            dic[i] -= 1
            if not dic[i]:
                del dic[i]
        return dic == {}
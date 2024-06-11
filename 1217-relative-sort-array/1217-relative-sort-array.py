class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = Counter(arr1)
        s = set(arr2)
        res = []
        for i in arr2:
            res += [i for _ in range(dic[i])]
        remaining = []
        for i in dic.keys():
            if i not in s:
                remaining += [i for _ in range(dic[i])]
        return res + sorted(remaining)
                
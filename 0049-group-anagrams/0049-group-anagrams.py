class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            sorted_str = str(sorted(string))
            if sorted_str in dic:
                dic[sorted_str].append(string)
            else:
                dic[sorted_str] = [string]
        res = []
        for key in dic.keys():
            res.append(dic[key])
        return res
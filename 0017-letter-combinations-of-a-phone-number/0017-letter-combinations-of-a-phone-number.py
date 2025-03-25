class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": ["a","b","c"]
            , "3": ["d","e","f"]
            , "4": ["g","h","i"]
            , "5": ["j","k","l"]
            , "6": ["m","n","o"]
            , "7": ["p","q","r", "s"]
            , "8": ["t","u","v"]
            , "9": ["w","x","y", "z"]}
        res = []
        for digit in digits:
            temp = dic[digit]
            if res == []:
                res = temp
            else:
                temp1 = []
                for i in res:
                    for j in temp:
                        temp1.append(i+j)
                res = temp1
        return res
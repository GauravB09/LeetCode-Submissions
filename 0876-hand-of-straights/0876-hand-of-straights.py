class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize != 0:
            return False
        dic = Counter(hand)
        sorted_keys = sorted(dic.keys())
        # print(dic, sorted_keys)
        for i in sorted_keys:
            count = dic[i]
            if count > 0:
                for j in range(groupSize):
                    # print(i, i+j, count, dic[i+j])
                    if dic[i+j] < count:
                        return False
                    dic[i+j] -= count
            # print(dic)
        return True
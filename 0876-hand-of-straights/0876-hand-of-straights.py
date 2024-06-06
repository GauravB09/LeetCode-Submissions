class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize != 0:
            return False
        dic = {}
        for num in hand:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        for _ in range(0, n, groupSize):
            start = min(dic)
            for j in range(groupSize):
                if start+j not in dic:
                    return False
                if dic[start+j] == 1:
                    dic.pop(start+j)
                else:
                    dic[start+j] -= 1
        return True
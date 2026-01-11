class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        curr_sum = 0
        banned = set(banned)
        result = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            curr_sum += i
            if curr_sum > maxSum:
                return result
            result += 1
        return result

        
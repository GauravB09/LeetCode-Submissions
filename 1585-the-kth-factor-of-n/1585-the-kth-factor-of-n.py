import math
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """   
        root = int(math.sqrt(n))
        count = 0
        res = []
        for i in range(1, root+1):
            if n % i == 0:
                count += 1
                res.append(i)
            if count == k:
                return res[-1]
        if root * root == n:
            return n // res[count-k-1] if count-k-1 >= -1*count else -1
        else:
            return n // res[count-k] if count-k >= -1 * count else -1
        return -1
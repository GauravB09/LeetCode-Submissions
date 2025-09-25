class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        lis = [triangle[-1][i] for i in range(n)]
        i = n - 1
        while i > 0:
            for j in range(i):
                lis[j] = min(lis[j], lis[j+1]) + triangle[i-1][j]
            # print(lis)
            i -= 1
        return lis[0]
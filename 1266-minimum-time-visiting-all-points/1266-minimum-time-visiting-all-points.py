class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        result = 0
        for i in range(1, n):
            curr = points[i]
            prev = points[i-1]
            result += max(abs(curr[0]-prev[0]), abs(curr[1]-prev[1]))
        return result
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        n = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, n):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        return res + [[start, end]]
            
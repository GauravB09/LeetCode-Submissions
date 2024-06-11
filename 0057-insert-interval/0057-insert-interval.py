class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        should_add, is_added = False, False
        for interval in intervals:
            # print(interval, should_add, is_added, newInterval)
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                should_add = True
                if not is_added:
                    res.append(newInterval)
                    is_added = True
                res.append(interval)
            else:
                should_add = True
                newInterval = [min(newInterval[0], interval[0]),max(newInterval[1], interval[1]) ]
        if not is_added:
            return res + [newInterval]
        return res
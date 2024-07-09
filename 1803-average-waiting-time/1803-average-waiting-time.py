class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitTime = 0
        startTime = 0
        count = 0
        for arrival, time in customers:
            count += 1
            if startTime < arrival:
                waitTime += time
                startTime = arrival + time
            else:
                startTime += time
                waitTime += startTime - arrival
        return float(waitTime / count)
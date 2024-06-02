class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        arr = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                arr[i] = max(arr[i], arr[i-1] + 1)
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)
        return sum(arr)
            




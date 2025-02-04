class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_Candies = max(candies)
        n = len(candies)
        result = [False] * n
        for i in range(n):
            if max_Candies - candies[i] <= extraCandies:
                result[i] = True
        return result

        
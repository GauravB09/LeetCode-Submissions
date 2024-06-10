class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i, j in zip(heights, expected):
            ans += int(i!=j)
        return ans
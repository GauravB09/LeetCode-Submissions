class Solution:
    def getNewNumber(self, mapping: List[int], num: str) -> int:
        ans = ""
        for i in num:
            ans += str(mapping[int(i)])
        return int(ans)

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=(lambda x : self.getNewNumber(mapping, str(x))))
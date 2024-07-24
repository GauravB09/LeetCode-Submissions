class Solution:
    # def getNewNumber(self, mapping: List[int], num: str) -> int:
    #     ans = ""
    #     for i in num:
    #         ans += str(mapping[int(i)])
    #     return int(ans)

    # def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    #     return sorted(nums, key=(lambda x : self.getNewNumber(mapping, str(x))))

    def getNewNumber(self, mapping: List[int], num: int) -> int:
        ans = 0
        place = 1
        if num == 0:
            return mapping[0]
        while num > 0:
            ans = (place * mapping[num%10]) + ans
            place *= 10
            num //= 10
        return ans

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=(lambda x : self.getNewNumber(mapping, x)))
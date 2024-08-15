class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_collected = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                bills_collected[5] += 1
            elif bill == 10:
                bills_collected[10] += 1
                bills_collected[5] -= 1
            elif bill == 20:
                if bills_collected[10] > 0:
                    bills_collected[10] -= 1
                    bills_collected[5] -= 1
                else:
                    bills_collected[5] -= 3
            if bills_collected[5] < 0 or bills_collected[10] < 0:
                return False
        return True

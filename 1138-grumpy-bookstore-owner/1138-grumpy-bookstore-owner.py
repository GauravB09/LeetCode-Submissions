class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        if n <= minutes:
            return sum(customers)
        max_val = 0
        for i in range(minutes):
            max_val += customers[i]
        for i in range(minutes, n):
            max_val += customers[i] * (1 - grumpy[i])
        ans = max_val
        for i in range(n - minutes):
            # print(max_val, customers[i+minutes], (customers[i] * (1 - grumpy[i])))
            max_val = max_val + (customers[i+minutes] * grumpy[i+minutes]) - (customers[i] * grumpy[i])
            ans = max(ans, max_val)
            # print(ans, max_val)
        return ans
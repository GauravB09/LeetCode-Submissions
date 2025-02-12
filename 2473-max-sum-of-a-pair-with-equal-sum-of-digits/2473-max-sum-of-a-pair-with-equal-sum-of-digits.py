class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getSumOfDigits(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res
        dictionary = {}
        for x in nums:
            sum_of_digits = getSumOfDigits(x)
            if sum_of_digits not in dictionary:
                dictionary[sum_of_digits] = [-1, -1]
            if x >= dictionary[sum_of_digits][0]:
                dictionary[sum_of_digits][1] = dictionary[sum_of_digits][0]
                dictionary[sum_of_digits][0] = x
            elif x >= dictionary[sum_of_digits][1]:
                dictionary[sum_of_digits][1] = x
        def func(lis):
            if lis[-1] == -1:
                return -1
            return lis[0] + lis[1]
        return max(map(func, dictionary.values()))

                

        
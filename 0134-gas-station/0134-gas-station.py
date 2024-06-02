class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_cost>total_gas:
            return -1
        fuel = 0
        ans = 0
        for i in range(n):
            fuel += gas[i]-cost[i]
            if fuel<0:
                fuel = 0
                ans = i+1
        return ans
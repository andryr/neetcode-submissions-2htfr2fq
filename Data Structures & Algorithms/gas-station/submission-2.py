class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        cur_gas = 0
        ans = 0
        for i in range(n):
            cur_gas += gas[i]
            cur_gas -= cost[i]
            if cur_gas < 0:
                ans = i + 1
                cur_gas = 0
        return ans

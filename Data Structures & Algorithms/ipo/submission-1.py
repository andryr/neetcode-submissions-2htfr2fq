class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = []
        profit_heap = []
        for profit, capital in zip(profits, capital):
            heapq.heappush(capital_heap, (capital, -profit))


        while k and (capital_heap or profit_heap):
            while capital_heap and capital_heap[0][0] <= w:
                capital, _profit = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, _profit)
            if k and profit_heap:
                _profit = heapq.heappop(profit_heap)
                w += -_profit
                k -= 1
            else:
                break
        return w
            
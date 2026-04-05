class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        seen = set()
        min_heap = []
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            if len(min_heap) == k and cnt[num] > min_heap[0][0]:
                heapq.heappop(min_heap)
            if len(min_heap) < k:
                heapq.heappush(min_heap, (cnt[num], num))
        return [v for k, v in min_heap]
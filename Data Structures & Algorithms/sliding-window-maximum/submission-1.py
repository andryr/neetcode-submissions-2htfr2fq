class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        max_heap = []
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            if right >= k - 1:
                while max_heap[0][1] < right - k + 1:
                    heapq.heappop(max_heap)
                ans.append(-max_heap[0][0])
        return ans

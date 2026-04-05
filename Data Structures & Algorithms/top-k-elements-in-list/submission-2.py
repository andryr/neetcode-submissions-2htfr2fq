class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        seen = set()
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            buckets[cnt[num]].append(num)
        ans = []
        for freq in range(len(nums), 0, -1):
            ans.extend(buckets[freq])
            if len(ans) == k:
                break
        return ans
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [key for key, val in sorted(cnt.items(), key=lambda x:-x[1])][:k]
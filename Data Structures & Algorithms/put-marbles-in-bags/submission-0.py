class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        consec_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        consec_sums.sort()
        print(consec_sums)
        min_score = sum(s for s in consec_sums[:k - 1])
        consec_sums.sort(reverse=True)
        max_score = sum(s for s in consec_sums[:k - 1])
        print(min_score, max_score)
        return max_score - min_score
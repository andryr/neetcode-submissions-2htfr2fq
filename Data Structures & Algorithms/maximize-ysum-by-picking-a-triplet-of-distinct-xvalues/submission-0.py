class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        x_to_y = defaultdict(int)
        for x_val, y_val in zip(x, y):
            x_to_y[x_val] = max(y_val, x_to_y[x_val])
        x, y = zip(*list(x_to_y.items()))
        if len(x) < 3:
            return -1
        idx = sorted(range(len(x)), key=lambda i: -y[i])
        return y[idx[0]] + y[idx[1]] + y[idx[2]]
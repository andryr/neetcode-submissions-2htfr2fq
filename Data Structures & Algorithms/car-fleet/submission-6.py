class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(sorted(zip(position, speed)))
        pairs.sort(reverse=True)
        ans = 1
        prev_ttr = (target - pairs[0][0]) / pairs[0][1]
        for i in range(1, len(pairs)):
            cur_ttr = (target - pairs[i][0]) / pairs[i][1]
            if cur_ttr > prev_ttr:
                prev_ttr = cur_ttr
                ans += 1
        return ans

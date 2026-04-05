class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        counter = Counter(hand)
        q = [(n, cnt) for n, cnt in counter.items()]
        heapq.heapify(q)
        while q:
            cur_group = [heapq.heappop(q)]
            for i in range(groupSize - 1):
                if not q or q[0][0] > cur_group[-1][0] + 1:
                    return False
                cur_group.append(heapq.heappop(q))
            for n, cnt in cur_group:
                if cnt > 1:
                    heapq.heappush(q, (n, cnt - 1))
        return True


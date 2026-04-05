class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        ans = [-1] * n
        entering = [(arrival[i], i) for i in range(n) if state[i] == 0]
        exiting = [(arrival[i], i) for i in range(n) if state[i] == 1]
        heapq.heapify(entering)
        heapq.heapify(exiting)
        cur_time = 0
        previous_use = None
        while entering or exiting:
            if entering:
                arrival_entering, i_entering = entering[0]
            else:
                arrival_entering = float("inf")
            if exiting:
                arrival_exiting, i_exiting = exiting[0]
            else:
                arrival_exiting = float("inf")

            arrival_entering = max(cur_time, arrival_entering)
            arrival_exiting = max(cur_time, arrival_exiting)

            if cur_time < min(arrival_entering, arrival_exiting):
                cur_time = min(arrival_entering, arrival_exiting)
                previous_use = None

            if arrival_entering < arrival_exiting or previous_use == 0 and arrival_entering == arrival_exiting:
                ans[i_entering] = cur_time
                previous_use = 0
                heapq.heappop(entering)
            elif arrival_exiting < arrival_entering or arrival_entering == arrival_exiting:
                ans[i_exiting] = cur_time
                previous_use = 1
                heapq.heappop(exiting)

            cur_time += 1

        return ans


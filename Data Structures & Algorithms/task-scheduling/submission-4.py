class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        schedule = []
        while max_heap or queue:
            if max_heap:
                _count, task = heapq.heappop(max_heap)
                schedule.append(task)
                count = - _count - 1
                if count:
                    queue.append((count, task, time + n + 1))
                time += 1
                while queue and queue[0][2] == time:
                    count, task, t = queue.popleft()
                    heapq.heappush(max_heap, (-count, task))
            else:
                count, task, t = queue.popleft()
                time = max(t, time)
                heapq.heappush(max_heap, (-count, task))
                while queue and queue[0][2] == time:
                    count, task, t = queue.popleft()
                    heapq.heappush(max_heap, (-count, task))


                
        return time

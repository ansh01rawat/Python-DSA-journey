class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        time = 0
        queue = deque()
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        for task, count in freq.items():
            heappush(heap, (-count, task))

        while heap or queue:
            time += 1
            while queue and queue[0][0] == time:
                _, count, task = queue.popleft()
                heappush(heap, (count, task))
            if heap:
                count, task = heappop(heap)
                count += 1
                if count < 0:
                    queue.append((time + n + 1, count, task))

        return time
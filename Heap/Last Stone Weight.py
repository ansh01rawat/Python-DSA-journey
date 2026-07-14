class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >= 2:
            largest = -heappop(stones)
            second = -heappop(stones)
            if largest != second:
                heappush(stones,(-(largest - second)))
        if stones:
            return -stones[0]
        else:
            return 0

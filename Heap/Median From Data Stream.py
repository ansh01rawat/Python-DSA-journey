class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                heappush(self.large, -heappop(self.small))
            else:
                heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if abs(len(self.small) - len(self.large)) <= 1:
            if len(self.small) > len(self.large):
                return -(self.small[0])
            elif len(self.small) < len(self.large):
                return self.large[0]
            else:
                return ((-self.small[0]) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
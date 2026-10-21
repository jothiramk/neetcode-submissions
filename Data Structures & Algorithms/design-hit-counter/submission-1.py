class HitCounter:

    def __init__(self):
        #define a sliding window - A queue
        self.window = deque()

    def hit(self, timestamp: int) -> None:
        self.window.append(timestamp)
        print(self.window)

        # while timestamp - self.window[0] >= 300:
        #     self.window.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.window and timestamp - self.window[0] >= 300:
            self.window.popleft()

        return len(self.window)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

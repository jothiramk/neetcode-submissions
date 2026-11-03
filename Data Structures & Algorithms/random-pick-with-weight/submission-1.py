class Solution:
#paypal pre just saw soln
    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)


    def pickIndex(self) -> int:
        target = self.total * random.random()
        curSum = 0
        for i in range(len(self.w)):
            curSum += self.w[i]
            
            if curSum > target:
                return i
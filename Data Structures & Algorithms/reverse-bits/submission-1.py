class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #find the ith bit
            res += (bit << (31 - i)) #and shift by 31-i to the new result
        return res
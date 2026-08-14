# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = 0
        h = n
        res = 0
        while l <= h:
            mid = (l+h)//2
            response = guess(mid)
            # print(f'my guess is {mid} and response from APi is {response}')
            if response == 0:
                return mid
            elif response == -1:
                h = mid -1
            else:
                l = mid+1

        return  0
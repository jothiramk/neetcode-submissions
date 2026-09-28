class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        number = 0
        i=10
        for digit in digits:
            number = number*i +digit
        
        # print(f'jothi {number}')
        number = number + 1
        while number:
            rem = number %10
            number = number //10
            res.append(rem)
        
        # print(f'ram {res}')
        return res[::-1]
        
        
            
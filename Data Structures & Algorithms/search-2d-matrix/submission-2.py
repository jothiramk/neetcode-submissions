class Solution:

    def binarySearch(self, row:List[int] , target : int) -> bool:
        low,high = 0, len(row)-1
        # print (row)
        while low <= high:
            mid = (low + high)//2
            print(f'{low} {high} {mid}')
            if row[mid] > target:
                high = mid - 1
            elif row[mid] < target:
                low = mid + 1
            elif row[mid]==target:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            res = self.binarySearch(row,target)
            if res:
                return True
        
        return False
        
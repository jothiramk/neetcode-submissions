class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0 
        h = (rows * cols) -1

        while l <= h:
            m = (l+h)//2
            row = m//cols
            col = m%cols
            # print(f'row is {row} and {col}')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                h = m -1
            else:
                l = m + 1
        return False
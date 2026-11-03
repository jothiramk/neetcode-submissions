class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        rows = len(matrix)
        cols = len(matrix[0])
        h = (rows * cols) -1

        while l <=h :
            m = (l+h)//2
            r = m // cols
            c = m % cols
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h =  m -1
            else:
                l = m + 1
        
        return False
            

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        h = rows*cols - 1 

        while  l <=h :
            m = (l+h)//2
            r = m//cols
            c = m % cols
            # print(f'middle is {m} and value {matrix[r][c]}')
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                l = m+1
            else:
                h = m -1
        
        return False
        

        
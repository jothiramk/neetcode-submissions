class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rows_status = [False] * rows
        cols_status = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    rows_status[r]=True
                    cols_status[c]=True

        # print(rows_status)
        # print(cols_status)

        for r in range(rows):
            for c in range(cols):
                if rows_status[r] or cols_status[c]:
                    matrix[r][c]=0

        
        
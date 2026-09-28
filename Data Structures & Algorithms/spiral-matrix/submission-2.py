class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left, top = 0, 0
        right, bottom = cols, rows

        res = []
        while left < right and top < bottom:
            # for every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top = top + 1
  
            # for every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right = right - 1
            print(f'res 2 {res} {left} {right} {top} {bottom}')
            if not (left < right and top < bottom):
                break

            # for every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom = bottom - 1
   
            # for every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left = left + 1


        return res


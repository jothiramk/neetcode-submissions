class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #greedy algo
        #flatten the matrix
        flat_matrix = []
        for row in range(len(matrix)):
            flat_matrix.extend(matrix[row])
        # print(flat_matrix)
        return self.binary_search(flat_matrix,target)
        
        

    def binary_search (self, matrix: list[int], target: int) -> bool:
        l = 0
        h = len(matrix)-1

        while l <= h:
            m = (h+l)//2
            # print(matrix[m])
            if matrix[m]==target:
                return True
            elif matrix[m]> target:
                h = m-1
            else:
                l = m+1
            
        return False
        
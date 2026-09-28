class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        quadrant = defaultdict(set)
        
        for r in range(rows):
            # print(f'processing row {r}')
            row_set = set()   
            for c in range(cols):
                # print(f'{board[r][c]}')
                if board[r][c].isdigit():
                    if board[r][c] in row_set:
                        return False
                    else:
                        row_set.add(board[r][c])
                    
                    #logic for checking quadrant
                    quadrant_key = (r//3,c//3)
                    value = quadrant[quadrant_key]
                    if board[r][c] in value:
                        return False
                    else:
                        quadrant[quadrant_key].add(board[r][c])
        # print(dict(quadrant))               


        for c in range(cols):
            col_set = set()  
            for r in range(rows):
                if board[r][c].isdigit():
                    if board[r][c] in col_set:
                        return False
                    else:
                        col_set.add(board[r][c])
        
        return True

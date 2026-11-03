class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        quadrant_map = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_map[r] or board[r][c] in col_map[c] or board[r][c] in quadrant_map[(r//3,c//3)]:
                    print(f'value of r {r} and c {c} and {board[r][c]}')
                    return False
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                quadrant_map[(r//3,c//3)].add(board[r][c])
        
        return True

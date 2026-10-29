class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        gridSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                rowQ = r//3
                colQ = c//3
                print((rowQ,colQ))
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in gridSet[(rowQ,colQ)]:
                    return False
                else:
                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    gridSet[(rowQ,colQ)].add(board[r][c])
                    # print(f'roset {rowSet}')
                    # print(f' colSet is {colSet}')
        return True

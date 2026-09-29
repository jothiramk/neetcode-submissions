class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCounter = defaultdict(set)
        colCounter = defaultdict(set)
        qudrantCounter = defaultdict(set)
        # print(rowCounter)
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range (cols):
                
                if board[r][c] == '.':
                    continue
                #row checks
                if board[r][c] in rowCounter[r]:
                    return False
                else:
                    rowCounter[r].add(board[r][c])
                #col checks
                if board[r][c] in colCounter[c]:
                    return False
                else:
                    colCounter[c].add(board[r][c])
                
                #quadrant checks
                rowQ = r//3
                colQ = c//3
                if board[r][c] in qudrantCounter[(rowQ,colQ)]:
                    return False
                else:
                    qudrantCounter[(rowQ,colQ)].add(board[r][c])

        
        return True
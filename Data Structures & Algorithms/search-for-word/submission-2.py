class Solution:
    def dfs(self, r : int, c : int ,board: List[List[str]], word: str,i : int ,rows,cols,visited) -> bool:

        # print(f'processing index i {i} and {r} and {c}')
        if min(r,c) < 0 or r >= rows or c >=cols or board[r][c] != word[i] or (r,c) in visited:
            # print(f'retruning {board[r][c]}')
            return False
        
        if i == len(word) - 1:
            # print('returning true here')
            return True
        
        visited.add((r,c))
        # print(visited)

        if self.dfs(r+1,c,board,word,i+1,rows,cols,visited):
            return True
        if self.dfs(r-1,c,board,word,i+1,rows,cols,visited):
            return True
        if self.dfs(r,c+1,board,word,i+1,rows,cols,visited):
            return True
        if self.dfs(r,c-1,board,word,i+1,rows,cols,visited):
            return True
        visited.remove((r,c))
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        #start from each cell and do a dfs
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if self.dfs(r,c,board,word,0,rows,cols,visited):
                    return True
        
        return False 
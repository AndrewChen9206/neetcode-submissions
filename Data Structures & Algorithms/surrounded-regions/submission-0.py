class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == 'X' or board[r][c] == 'T':
                return
            
            board[r][c] = 'T'

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][len(board[0])-1] == 'O':
                dfs(r, len(board[0])-1)
        
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[len(board)-1][c] == 'O':
                dfs(len(board)-1, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
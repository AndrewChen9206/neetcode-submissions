class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [['.'] * n for _ in range(n)]
        col_set = set()
        diag_1 = set()
        diag_2 = set()

        def insertInRow(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col not in col_set and (row - col) not in diag_1 and (row + col) not in diag_2:
                    board[row][col] = 'Q'
                    col_set.add(col)
                    diag_1.add(row - col)
                    diag_2.add(row + col)

                    insertInRow(row + 1)

                    board[row][col] = '.'
                    col_set.remove(col)
                    diag_1.remove(row - col)
                    diag_2.remove(row + col)
                
        insertInRow(0)

        return res
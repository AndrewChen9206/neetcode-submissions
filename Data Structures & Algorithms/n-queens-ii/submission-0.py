class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        col_set = set()
        diag_1 = set()
        diag_2 = set()

        def insertInRow(row):
            if row == n:
                self.res += 1
                return

            for col in range(n):
                if col not in col_set and (row - col) not in diag_1 and (row + col) not in diag_2:
                    col_set.add(col)
                    diag_1.add(row - col)
                    diag_2.add(row + col)

                    insertInRow(row + 1)

                    col_set.remove(col)
                    diag_1.remove(row - col)
                    diag_2.remove(row + col)
                
        insertInRow(0)

        return self.res
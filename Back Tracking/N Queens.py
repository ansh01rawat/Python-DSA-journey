class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []
        cols = set()
        diag = set()
        anti = set()

        def dfs(row):
            if row == n:
                solution = ["".join(row) for row in board]
                result.append(solution)
                return
            for col in range(n):
                if col in cols:
                    continue
                if (row - col) in diag:
                    continue
                if (row + col) in anti:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                diag.add(row - col)
                anti.add(row + col)
                dfs(row + 1)
                board[row][col] = "."
                cols.remove(col)
                diag.remove(row - col)
                anti.remove(row + col)

        dfs(0)
        return result


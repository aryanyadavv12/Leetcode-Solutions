class Solution:
    #Aryan
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        Min = [[inf] * n for _ in range(m)]
        Max = [[-inf] * n for _ in range(m)]
        Min[0][0], Max[0][0] = grid[0][0], grid[0][0]
        for i in range(m):
            for j in range(n):
                if  i == 0 and j == 0:
                    continue
                Min[i][j] = min(
                    Min[i - 1][j] * grid[i][j] if i > 0 else inf,
                    Max[i - 1][j] * grid[i][j] if i > 0 else inf,
                    Min[i][j - 1] * grid[i][j] if j > 0 else inf,
                    Max[i][j - 1] * grid[i][j] if j > 0 else inf
                )
                Max[i][j] = max(
                    Min[i - 1][j] * grid[i][j] if i > 0 else -inf,
                    Max[i - 1][j] * grid[i][j] if i > 0 else -inf,
                    Min[i][j - 1] * grid[i][j] if j > 0 else -inf,
                    Max[i][j - 1] * grid[i][j] if j > 0 else -inf
                )
            
        res = Max[-1][-1]
        return res % MOD if res >= 0 else -1
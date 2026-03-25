class Solution:
    #Aryan
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        n = len(grid)
        m = len(grid[0])
        zero = 0
        total = 1
        mod = 12345
        for i in range(n):
            for j in range(m):
                grid[i][j] %= mod
                if grid[i][j] == 0:
                    zero += 1
                else:
                    total = total * grid[i][j]

        for i in range(n):
            for j in range(m):
                if zero > 1:
                    grid[i][j] = 0
                elif zero == 1:
                    if grid[i][j]:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = total % mod
                else:
                    grid[i][j] = (total // grid[i][j]) % mod
        return grid
        """
        
        
        n = len(grid)
        m = len(grid[0])
        zero = 0
        total = 1
        dp = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = total
                total = (total * grid[i][j]) % 12345
        total = 1
        for i in range(n):
            for j in range(m):
                dp[i][j] = (dp[i][j] * total) % 12345
                total = (total * grid[i][j]) % 12345
        return dp
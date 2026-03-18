class Solution:
    #Aryan
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r = len(grid)
        c = len(grid[0])
        cols = [0] * c
        res = 0
        for i in range(r):
            row_sum = 0
            for j in range(c):
                cols[j] += grid[i][j]
                row_sum += cols[j]
                if row_sum <= k:
                    res += 1
        return res
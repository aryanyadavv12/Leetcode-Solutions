class Solution:
    #Aryan
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        res = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]
        def diff(window):
            if len(window) < 2:
                return 0
            min_diff = float('inf')
            for i in range(len(window) - 1):
                diff = window[i + 1] - window[i]
                if diff > 0 and diff < min_diff:
                    min_diff = diff
            return min_diff if min_diff != float('inf') else 0
        for r in range(rows - k + 1):
            cur = []
            for i in range(k):
                for j in range(k):
                    insort(cur, grid[r+i][j])
            res[r][0] = diff(cur)
            for c in range(1, cols - k + 1):
                for i in range(k):
                    remove = grid[r+i][c-1]
                    index = bisect_left(cur, remove)
                    cur.pop(index)
                for i in range(k):
                    add = grid[r+i][c+k-1]
                    insort(cur, add)
                res[r][c] = diff(cur)
        return res
            
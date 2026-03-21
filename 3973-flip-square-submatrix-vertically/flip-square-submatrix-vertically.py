class Solution:
    #Aryan
    def reverseSubmatrix(self, grid, x, y, k):
        nx = x + k - 1
        ny = y + k - 1
        s, e = x, nx
        while s < e:
            for col in range(y, ny + 1):
                grid[s][col], grid[e][col] = grid[e][col], grid[s][col]
            s += 1
            e -= 1
        return grid
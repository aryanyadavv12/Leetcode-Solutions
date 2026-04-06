class Solution:
    #Aryan
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y, = 0, 0
        res = 0
        hash_set = set()
        for a, b in obstacles:
            hash_set.add((a, b))

        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                for i in range(c):
                    ox= x + dirs[d][0]
                    oy = y + dirs[d][1]
                    if (ox, oy) in hash_set:
                        break
                    res = max(res, ox**2 + oy**2)
                    x, y = ox, oy
        return res

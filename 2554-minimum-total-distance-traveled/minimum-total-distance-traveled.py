from functools import lru_cache

class Solution:
    #Aryan
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)

        @lru_cache(maxsize=None)
        def fn(i: int, j: int) -> int:
            if i == 0:
                return 0
            if j == 0:
                return float('inf')

            skip_factory = fn(i, j - 1)
            pick_factory = float('inf')
            distance = 0
            pos, limit = factory[j - 1]

            for robots_serviced in range(1, limit + 1):
                if i - robots_serviced < 0:
                    break
                distance += abs(robot[i - robots_serviced] - pos)
                cost = fn(i - robots_serviced, j - 1) + distance
                pick_factory = min(pick_factory, cost)

            return min(skip_factory, pick_factory)

        return fn(n, m)
class Solution:
    #Aryan
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robot_info = list(zip(robots, distance))
        robot_info.sort()
        walls.sort()
        n = len(robots)

        wall_left = [0] * n
        for i in range(n):
            pre_bot_pos = robot_info[i-1][0] if i > 0 else -float("inf")
            left_index = max(robot_info[i][0] - robot_info[i][1], pre_bot_pos+1)
            wall_left[i] = bisect.bisect_right(walls, robot_info[i][0]) - bisect.bisect_left(walls, left_index)

        wall_right = [0] * n
        for i in range(n):
            next_bot_pos = robot_info[i+1][0] if i < n-1 else float("inf")
            right_index = min(robot_info[i][0] + robot_info[i][1], next_bot_pos-1)
            wall_right[i] = bisect.bisect_right(walls, right_index) - bisect.bisect_left(walls, robot_info[i][0])

        wall_intesect = [0] * n
        for i in range(1, n):
            cur_left_index = left_index = max(robot_info[i][0] - robot_info[i][1], robot_info[i-1][0]+1)
            pre_right_index = min(robot_info[i-1][0] + robot_info[i-1][1], robot_info[i][0]-1)
            if cur_left_index > pre_right_index:
                wall_intesect[i] = 0
            else:
                wall_intesect[i] =  bisect.bisect_right(walls, pre_right_index) - bisect.bisect_left(walls, cur_left_index)

        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = wall_left[0]
        dp[0][1] = wall_right[0]
        for i in range(1, n):

            dp[i][0] = max(wall_left[i]+dp[i-1][0], wall_left[i]+dp[i-1][1]-wall_intesect[i])

            dp[i][1] = wall_right[i] + max(dp[i-1][0], dp[i-1][1])
        return max(dp[n-1])



        
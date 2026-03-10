class Solution:
    #Aryan
    def numberOfStableArrays(self, zeros: int, ones: int, limit: int) -> int:

        MOD = 10**9 + 7

        dp = [[[0]*2 for _ in range(ones+1)] for _ in range(zeros+1)]

        dp[0][0][0] = 1
        dp[0][0][1] = 1

        for i in range(zeros+1):
            for j in range(ones+1):

                if i == 0 and j == 0:
                    continue

                endWithZero = 0
                endWithOne = 0

                if j > 0:
                    endWithZero = dp[i][j-1][1]

                    if j > 1:
                        endWithZero = (endWithZero + dp[i][j-1][0]) % MOD

                    if j > limit:
                        endWithZero = (endWithZero - dp[i][j-1-limit][1] + MOD) % MOD

                if i > 0:
                    endWithOne = dp[i-1][j][0]

                    if i > 1:
                        endWithOne = (endWithOne + dp[i-1][j][1]) % MOD

                    if i > limit:
                        endWithOne = (endWithOne - dp[i-1-limit][j][0] + MOD) % MOD

                dp[i][j][0] = endWithZero % MOD
                dp[i][j][1] = endWithOne % MOD

        return (dp[zeros][ones][0] + dp[zeros][ones][1]) % MOD
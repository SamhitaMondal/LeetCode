class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(grid[0])


        dp = [1] + [0] * (n - 1)

        for row in grid:
            left = 0

            for j in range(n):
                if row[j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    left = dp[j] = (left + dp[j]) % MOD

        return left


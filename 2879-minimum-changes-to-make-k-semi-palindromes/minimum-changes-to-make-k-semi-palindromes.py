class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = float('inf')

        # Part A: Precompute substring costs

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                length = j - i + 1
                best = INF

                for d in range(1, length):

                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):

                        left = i + offset
                        right = j - d + 1 + offset

                        while left < right:

                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # Part B: Dynamic Programming

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):

            for j in range(1, k + 1):

                for end in range(i + 1, n):

                    dp[i][j] = min(
                        dp[i][j],
                        cost[i][end] + dp[end + 1][j - 1]
                    )

        return dp[0][k]
class Solution {
    public int numberOfSets(int n, int k) {

        int MOD = 1000000007;

        long[][] dp = new long[k + 1][n];

        // 0 segments = 1 way
        for (int i = 0; i < n; i++) {
            dp[0][i] = 1;
        }

        for (int j = 1; j <= k; j++) {

            long sum = 0;

            for (int i = 1; i < n; i++) {

                // Add dp[j-1][i-1] to the running sum
                sum = (sum + dp[j - 1][i - 1]) % MOD;

                // Don't use i OR create a segment ending at i
                dp[j][i] = (dp[j][i - 1] + sum) % MOD;
            }
        }

        return (int) dp[k][n - 1];
    }
}
class Solution {

    public int maxPalindromes(String s, int k) {

        int n = s.length();

        int[] dp = new int[n + 1];

        for (int i = 0; i < n; i++) {

            // Skip this character
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);

            // Try palindrome starting at i
            for (int j = i + k - 1; j < n; j++) {

                if (isPalindrome(s, i, j)) {

                    dp[j + 1] =
                        Math.max(dp[j + 1], dp[i] + 1);

                    break;
                }
            }
        }

        return dp[n];
    }


    private boolean isPalindrome(String s, int l, int r) {

        while (l < r) {

            if (s.charAt(l) != s.charAt(r))
                return false;

            l++;
            r--;
        }

        return true;
    }
}
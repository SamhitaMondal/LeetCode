class Solution {

    Set<String> result = new HashSet<>();

    public List<String> removeInvalidParentheses(String s) {

        int left = 0;
        int right = 0;

        // Find minimum number of '(' and ')' to remove
        for (char c : s.toCharArray()) {

            if (c == '(') {
                left++;
            } 
            else if (c == ')') {

                if (left > 0) {
                    left--;
                } 
                else {
                    right++;
                }
            }
        }

        backtrack(s, 0, left, right, 0, "");

        return new ArrayList<>(result);
    }

    void backtrack(String s, int index,
                   int leftRemove, int rightRemove,
                   int balance, String current) {

        // Invalid
        if (balance < 0) {
            return;
        }

        // Reached end
        if (index == s.length()) {

            if (leftRemove == 0 &&
                rightRemove == 0 &&
                balance == 0) {

                result.add(current);
            }

            return;
        }

        char c = s.charAt(index);

        // Parenthesis
        if (c == '(') {

            // Option 1: remove '('
            if (leftRemove > 0) {
                backtrack(
                    s,
                    index + 1,
                    leftRemove - 1,
                    rightRemove,
                    balance,
                    current
                );
            }

            // Option 2: keep '('
            backtrack(
                s,
                index + 1,
                leftRemove,
                rightRemove,
                balance + 1,
                current + c
            );
        }

        else if (c == ')') {

            // Option 1: remove ')'
            if (rightRemove > 0) {
                backtrack(
                    s,
                    index + 1,
                    leftRemove,
                    rightRemove - 1,
                    balance,
                    current
                );
            }

            // Option 2: keep ')'
            if (balance > 0) {
                backtrack(
                    s,
                    index + 1,
                    leftRemove,
                    rightRemove,
                    balance - 1,
                    current + c
                );
            }
        }

        else {

            // Letter → always keep
            backtrack(
                s,
                index + 1,
                leftRemove,
                rightRemove,
                balance,
                current + c
            );
        }
    }
}
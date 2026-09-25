class Solution {
    public List<String> braceExpansionII(String expression) {
        Set<String> result = parse(expression, 0, expression.length()).set;
        
        List<String> ans = new ArrayList<>(result);
        Collections.sort(ans);
        return ans;
    }

    static class Result {
        Set<String> set;
        int index;

        Result(Set<String> set, int index) {
            this.set = set;
            this.index = index;
        }
    }

    private Result parse(String s, int i, int n) {

        Set<String> result = new HashSet<>();
        Set<String> current = new HashSet<>();
        current.add("");

        while (i < n && s.charAt(i) != '}') {

            char ch = s.charAt(i);

            if (ch == ',') {
                // Union
                result.addAll(current);
                current = new HashSet<>();
                current.add("");
                i++;
            }

            else if (ch == '{') {
                // Parse the expression inside {}
                Result inside = parse(s, i + 1, n);

                current = concatenate(current, inside.set);

                i = inside.index + 1;
            }

            else {
                // Normal character
                Set<String> letter = new HashSet<>();
                letter.add(String.valueOf(ch));

                current = concatenate(current, letter);

                i++;
            }
        }

        // Add the last part
        result.addAll(current);

        return new Result(result, i);
    }

    private Set<String> concatenate(Set<String> a, Set<String> b) {

        Set<String> result = new HashSet<>();

        for (String x : a) {
            for (String y : b) {
                result.add(x + y);
            }
        }

        return result;
    }
}
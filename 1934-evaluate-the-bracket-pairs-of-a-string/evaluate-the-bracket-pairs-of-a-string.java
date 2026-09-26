class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        HashMap<String, String>map=new HashMap<>();
        //Store key-value pairs
        for(List<String> pair: knowledge){
            map.put(pair.get(0),pair.get(1));
        }
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '(') {

                int j = i + 1;

                // Find closing bracket
                while (s.charAt(j) != ')') {
                    j++;
                }

                // Extract key
                String key = s.substring(i + 1, j);

                // Get value or ?
                if (map.containsKey(key)) {
                    result.append(map.get(key));
                } else {
                    result.append("?");
                }

                // Move i to ')'
                i = j;

            } else {
                result.append(s.charAt(i));
            }
        }

        return result.toString();
    }
}
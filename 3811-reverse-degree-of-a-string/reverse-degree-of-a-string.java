class Solution {
    public int reverseDegree(String s) {
        int ans=0;
        int n = s.length();
        for(int i=0;i<n;i++){
            char x=s.charAt(i);
            int rev='z'-x+1;
            ans+=rev*(i+1);
        }
        return ans;
    }
}
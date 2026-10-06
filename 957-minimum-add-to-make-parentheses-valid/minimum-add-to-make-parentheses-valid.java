class Solution {
    public int minAddToMakeValid(String s) {
        int depth=0;
        int c=0;
        for(int i=0;i<s.length();i++){
           if(s.charAt(i)=='('){
              depth++;
            }
           
           else{
            if(depth>0){
              depth--;
            }
            else{
                c++;
            }
           }
           
        }
        return c+depth; 
    }
}    
        
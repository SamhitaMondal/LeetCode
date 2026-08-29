class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int idx[]=new int[2];
        int s=0;
        int e=numbers.length-1;
        while(s<e){
            if(numbers[s]+numbers[e]==target){
                idx[0]=s+1;
                idx[1]=e+1;
                return idx;
            }
            else if(numbers[s]+numbers[e]<target){
                s++;
            }
            else{
                e--;
            }
        }
        return idx;
    }
    
}
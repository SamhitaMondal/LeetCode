class Solution {
    public int[] sortedSquares(int[] nums) {
        int s_arr[]=new int[nums.length];
        int ptr=nums.length-1;
        int s=0;
        int e=nums.length-1;
        while(e>=s){
            int ss=nums[s]*nums[s];
            int es=nums[e]*nums[e];
            if(ss>es){
               s_arr[ptr]=ss;
               s++;
            }
            else{
                s_arr[ptr]=es;
                e--;
            }
            ptr--;
        }
        return s_arr;
    }
}
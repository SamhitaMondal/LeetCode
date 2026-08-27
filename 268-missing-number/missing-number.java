class Solution {
    public int missingNumber(int[] nums) {
       int n=nums.length;
       int a_sum=(n*(n+1))/2;
       int c_sum=0;
       for(int i=0;i<nums.length;i++){
        c_sum+=nums[i];
       }
       int m=a_sum-c_sum;
       return m;
    }
}
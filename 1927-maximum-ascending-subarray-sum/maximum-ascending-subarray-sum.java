class Solution {
    public int maxAscendingSum(int[] nums) {
        int max=0;
        
        
        for(int i=0;i<nums.length;i++){
            int c_max=nums[i];
            
            
            
            for(int j=i+1;j<nums.length;j++){
                if(nums[j]>nums[j-1]){
                  c_max+=nums[j];
                }
                else{
                    break;
                } 
            }
            if(c_max>max){
                max=c_max;
            }
        }
        return max;
    }
}
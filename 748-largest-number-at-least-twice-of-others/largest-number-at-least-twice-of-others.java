class Solution {
    public int dominantIndex(int[] nums) {
        int max=-1;
        int s_max=-1;
        int idx=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>max){
                s_max=max;
                max=nums[i];
                idx=i;
            }
            else if(nums[i]>s_max){
                s_max=nums[i];
            }
        }
        if(s_max*2<=max){
            return idx;
        }
        else{
            return -1;
        }
    }
}
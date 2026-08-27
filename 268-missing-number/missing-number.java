class Solution {
    public int missingNumber(int[] nums) {
        int freq[]=new int[nums.length+1];
        for(int i=0;i<nums.length;i++){
            freq[i]=0;
        }
        
        for(int i=0;i<=nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(i==nums[j]){
                    freq[i]++;
                }
                
            }
        }
        for(int i=0;i<=nums.length;i++){
            if(freq[i]==0){
                return i;
            }
        }
       return -1;
    }
}
class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n=arr.length;
        int INF=1000000;
        //dp[i]=shortest target subarray before index i
        int []dp=new int[n+1];
        for(int i=0;i<=n;i++){
            dp[i]=INF;
        }
        int  ans=INF;
        int left=0;
        int sum=0;
        int best=INF;
        for(int right=0;right<n;right++){
            sum+=arr[right];
            //Shrink window if sum becomes too large
            while(sum>target){
                sum-=arr[left];
                left++;
            }
            //We found a subarray with sum= target
            if(sum==target){
                int len=right-left+1;
                //Is theere a previous non-overlapping subarray?
                if(dp[left]!=INF){
                    ans=Math.min(ans,len+dp[left]);
                }
                //This is the best subarray ending at/before right
                best=Math.min(best,len);
            }
            dp[right+1]=best;
        }
        return ans==INF ?-1:ans;
    }
}
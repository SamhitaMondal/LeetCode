class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        min_sum=float('inf')
        for i in range(n):
            curr_sum=0
            for j in range(i,min(n,i+r)):
                curr_sum+=nums[j]
                length=j-i+1
                if length>=l and curr_sum>0:
                    min_sum=min(min_sum,curr_sum)
        if min_sum==float('inf'):
            return -1
        return min_sum                

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i in range(n):
            s=set()
            for j in range(i,n):
                s.add(nums[j])
                sum+=len(s)*len(s)
        return sum        

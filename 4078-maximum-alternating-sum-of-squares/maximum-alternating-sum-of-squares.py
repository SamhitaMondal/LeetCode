class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x*x)
        n=len(nums)
        score=0
        for i in range(n):
            if i<n//2: #smaller half is subtracted and larger half is addes
                score-=nums[i]*nums[i]
            else:
                score+=nums[i]*nums[i]
        return score            
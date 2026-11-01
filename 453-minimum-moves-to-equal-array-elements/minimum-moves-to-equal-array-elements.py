class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum=min(nums)
        m=0
        for i in range (len(nums)):
            m+=nums[i]-minimum
        return m    
        
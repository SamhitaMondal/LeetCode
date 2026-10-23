class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k=-1
        for i in range(len(nums)):
            if nums[i]!=i:
                if k==-1:
                    k=nums[i]
                else:
                    k &=nums[i]
        return max(k,0)                  
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        res = nums[0]
        
        
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] >= 0 else 0
            res = max(res, nums[i])
            
        return res
            
        
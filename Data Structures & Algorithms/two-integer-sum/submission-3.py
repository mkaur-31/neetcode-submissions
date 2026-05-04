class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i, num in enumerate(nums):
            comp = target-num
            if comp in ref:
                return [ref[comp],i]
            else:
                ref[num] = i
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref_dict={}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in ref_dict:
                return [ref_dict[comp],i]
            else:
                ref_dict[nums[i]] = i
        
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        res = 0
        for num in nums:
            if num-1 in lookup:
                pass
            else: 
                length = 1
                while True:
                    if num + 1 not in lookup:
                        res = max(length, res)
                        break
                    length += 1
                    num = num+1
        


        return res
                
        
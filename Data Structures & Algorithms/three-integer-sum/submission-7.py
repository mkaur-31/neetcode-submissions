from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i,a in enumerate(nums):
            if a>0:
                break

            if i>0 and a == nums[i-1]:
                continue

            j,k= i+1,len(nums)-1
            target = 0 - a

            while j<k:
                temp = nums[j] + nums[k]
                if temp == target:                                   
                    res.append([a,nums[j],nums[k]])  
                    j +=1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif temp < target:
                    j+=1
                else: 
                    k-=1
        print(res)
        return res
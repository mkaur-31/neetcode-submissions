from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            j,k= i+1,len(nums)-1
            target = 0 - nums[i]

            while j<k:
                temp = nums[j] + nums[k]
                if temp == target:                                   
                    res.append([nums[i],nums[j],nums[k]])  
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
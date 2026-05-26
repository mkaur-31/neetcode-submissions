from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for h in range(len(nums)-2):
            if h>0 and nums[h] == nums[h-1]:
                continue
            i,j= h+1,len(nums)-1
            target = 0 - (nums[h])

            while i<j:
                temp = nums[i] + nums[j]
                if temp == target:                                   
                    res.append([nums[h],nums[i],nums[j]])  
                    i +=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                elif temp < target:
                    i+=1
                else: 
                    j-=1
        print(res)
        return res
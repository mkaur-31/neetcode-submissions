class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flag = False
        idx = []
        prod = 1
        for i,x in enumerate(nums):
            if x == 0:
                flag = True
                idx.append(i)
                continue
            prod *= x
        if flag == False:
            return [prod//y for y in nums]
        else: 

 
            result = [0]* len(nums)
            if len(idx) == 1 :
                for i in idx:
                    result[i] = prod
            return result


    
        
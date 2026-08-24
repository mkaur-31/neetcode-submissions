class Solution:
    def climbStairs(self, n: int) -> int:
        t1 = 1
        t2 = 1
        res = 1
        for i in range(2, n+1):
            res = t1 + t2
            t1,t2 = t2,res
        return res
        
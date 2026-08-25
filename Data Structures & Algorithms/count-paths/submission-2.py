class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[1]*n
        print(dp)     
        for i in range(1,m):
            new_dp = dp
            for j in range(1,n):
                    new_dp[j] += new_dp[j-1]
            dp = new_dp
                
                   
        return dp[-1]

        
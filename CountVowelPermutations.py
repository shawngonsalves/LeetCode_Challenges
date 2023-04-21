class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[],[1,1,1,1,1]]

        a,e,i,o,u = 0,1,2,3,4
        mod = 10 ** 9 + 7

        for j in range(2, n+1):
            dp.append([0,0,0,0,0])
            dp[j][0] = (dp[j-1][1] +dp[j-1][2] + dp[j-1][4]) % mod
            dp[j][1] =(dp[j-1][0] + dp[j-1][2]) % mod
            dp[j][2] = (dp[j-1][1]+dp[j-1][3]) % mod
            dp[j][3] = (dp[j-1][2]) % mod
            dp[j][4] = (dp[j-1][2]+dp[j-1][3]) % mod
        return sum(dp[n]) % mod

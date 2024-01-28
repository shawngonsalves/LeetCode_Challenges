'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Constraints:

1 <= n <= 1000
0 <= k <= 1000
'''

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # time limit exceeded
        # mod = 10 **9 + 7
        # cache = {}
        # def count(n, k):
        #     if n == 0:
        #         return 1 if k == 0 else 0
        #     if k < 0:
        #         return 0
        #     if (n, k) in cache:
        #         return cache[(n, k)]
            
        #     for i in range(n):
        #         cache[(n, k)] = ((cache[(n, k)] + count(n -1, k - i)) % mod)
               
        #     return cache[(n, k)]
        # return count(n, k)

#=======================================================
        # mod = 10 **9 + 7
        # dp = [[0] * (k+1) for _ in range(n+1)]
        # dp[0][0] = 1

        # for N in range(1, n+1):
        #     for K in range(k+1):
        #         for pairs in range(N):
        #             if k - pairs >= 0:
        #                 dp[N][K] += dp[N-1][K - pairs]
        # return dp[n][k]
#=======================================================

        # mod = 10 **9 + 7
        # dp = [0] * (k+1)
        # dp[0] = 1

        # for N in range(1, n+1):
        #     cur = dp = [0] * (k+1)
        #     for K in range(k+1):
        #         for pairs in range(N):
        #             if k - pairs >= 0:
        #                 cur[K] += dp[K - pairs]
        #     dp = cur
        # return dp[n][k]
#=========================================================
#sliding window
        mod = 10**9 + 7
        dp = [0] * (k+1)
        dp[0] = 1

        for N in range(1, n+1):
            cur = [0] * (k+1)
            total = 0
            for K in range(0, k+1):               
                if K >= N:
                    total -= dp[K-N]
                total = (total + dp[K]) % mod
                cur[K] = total
                    
            dp = cur
        return dp[k]

'''
Runtime 145 ms Beats 100.00% of users with Python3
Memory 16.67 MB Beats 86.96% of users with Python3
'''
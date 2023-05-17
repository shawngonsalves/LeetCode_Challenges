class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        # dp = {}

        # def dfs(i,j):
        #     if len(nums1) ==i or j == len(nums2):
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     if nums1[i] == nums2[j]:
        #         dp[(i,j)] = 1 + dfs(i+1,j+1)

        #     else:
        #         dp[(i,j)] = max(dfs(i+1,j), dfs(i,j+1))
        #     return dp[(i,j)]
        # return dfs(0,0)

        prev = [0] * (len(nums2)+1)

        for i in range(len(nums1)):
            dp = [0] * (len(nums2)+1)
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[j+1] = 1 + prev[j]
                else:
                    dp[j+1] = max(prev[j+1], dp[j])
            prev = dp

        return dp[len(nums2)]

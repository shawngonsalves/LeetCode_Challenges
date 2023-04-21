class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i,even)]
            total = nums[i] if even else(-1 * nums[i])
            
            dp[(i, even)] = max(total+ dfs(i+1, not even), dfs(i+1, even))

            return dp[(i,even)]
        
        return dfs(0, True)

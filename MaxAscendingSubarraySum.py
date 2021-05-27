class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        maxyet = 0
        for i in range(len(nums)):
            if nums[i] <= nums[i-1]:
                res = max(res, maxyet)
                maxyet = 0
            maxyet += nums[i]
        return max(res,maxyet)
    

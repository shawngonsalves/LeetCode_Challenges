class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max_yet = nums[0]
        for i in range(1,len(nums)):
            max_sum = max(max_sum+nums[i],nums[i])
            print(max_sum)
            max_yet = max(max_yet,max_sum)
            print(max_yet)
        return max_yet
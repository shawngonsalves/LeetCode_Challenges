# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

 

# Example 1:

# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
# Example 2:

# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.
 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i] <= 106
class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        #Bottom-up DP 
        two = nums[-1] == nums[-2]
         
        if len(nums) == 2:
            return two
        
        three = (nums[-3] == nums[-2] == nums[-1] or 
                nums[-3] + 1 == nums[-2] == nums[-1] - 1)

        dp = [three,two,False]

        for i in range(len(nums) -4, -1, -1):
            cur = (nums[i] == nums[i+1]) and dp[1]  #dp[1] because we are shifting by 2
            cur = cur or ((nums[i] == nums[i+1] == nums[i+2] or 
            nums[i] + 1 == nums[i+1] == nums[i+2] - 1) and dp[2])
            dp = [cur, dp[0], dp[1]]

        return dp[0]

# Runtime 871 ms Beats 63.67%
# Memory 30.4 MB Beats 75.13%
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return (nums[0]*nums[1]*nums[2])
        nums = sorted(nums)

        neghalf = nums[:3]
        poshalf = nums[-3:]

        return max(neghalf[0]*neghalf[1]*poshalf[-1], poshalf[0]*poshalf[1]*poshalf[2])

# Runtime 224 ms Beats 94.97%
# Memory 17.5 MB Beats 84.1%
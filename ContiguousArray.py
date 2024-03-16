'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0

        longest = 0
        diff_index = {} # count[1] - count[0] -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            diff = one - zero
            if diff not in diff_index:
                diff_index[diff] = i
            if one == zero:
                longest = one + zero

            else:
                idx = diff_index[diff]
                longest = max(longest, i - idx)

        return longest
    
'''
Runtime 835 ms Beats 5.03% of users with Python3
Memory 21.37 MB Beats 98.53% of users with Python3
'''
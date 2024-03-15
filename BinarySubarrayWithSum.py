'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(x):
            if x < 0:
                return 0
            l = 0
            cur_sum = 0
            res = 0
            for r in range(len(nums)):
                cur_sum += nums[r]

                while cur_sum > x:
                    cur_sum -= nums[l]
                    l += 1

                res += (r -l + 1)
            return res
            
        return helper(goal) - helper(goal -1)
    
'''
Runtime 228 ms Beats 33.74% of users with Python3
Memory 17.26 MB Beats 96.41% of users with Python3
'''
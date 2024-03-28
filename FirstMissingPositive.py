'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            while True:
                val = nums[i]

                if val <= 0 or val > N or val == nums[val-1]:
                    break
                nums[i], nums[val-1] = nums[val-1], nums[i]

        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1

'''
Runtime 297 ms Beats 53.59% of users with Python3
Memory 30.25 MB Beats 81.04% of users with Python3
'''
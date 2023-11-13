'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


'''
Runtime 75 ms Beats 65.96%
Memory 16.9 MB Beats 86.28%
'''
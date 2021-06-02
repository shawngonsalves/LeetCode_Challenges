'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        print(count)
        for i in range(count):
            if 0 in nums:
                nums.remove(0)
       
        for i in range(count):
            nums.append(0)

        return nums

'''
Success
Details 
Runtime: 124 ms, faster than 14.51% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 16.59% of Python3 online submissions for Move Zeroes.
Next challenges:
'''
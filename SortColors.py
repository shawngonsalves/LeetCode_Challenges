'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        r = len(nums)-1
        
        i = 0
        
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <=r:
            if nums[i] ==0:
                swap(i,l)
                l+=1
            if nums[i] ==2:
                swap(i,r)
                r-=1
                i-=1
            i+=1

'''
Runtime: 32 ms, faster than 76.07% of Python3 online submissions for Sort Colors.
Memory Usage: 14.1 MB, less than 73.01% of Python3 online submissions for Sort Colors.
'''
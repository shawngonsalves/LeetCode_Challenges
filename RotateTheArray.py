'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        def helper(l,r):
            while l < r:
                nums[l], nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        l = 0
        r = len(nums)-1
        print(nums)

        helper(l,r)
        print(nums)
        l = 0
        r = k-1
        helper(l,r)
        print(nums)
        l = k
        r = len(nums)-1
        helper(l,r)

'''
Runtime: 264 ms, faster than 30.40% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 54.94% of Python3 online submissions for Rotate Array.
'''
'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        a = b = nums[0]

        while True:
            a = nums[a]
            print("tortoise",a)
            b = nums[nums[b]]
            print("hare",b)
            if a == b:
                break
        print('herenowwww')
        # Find the "entrance" to the cycle.
        print('nums0: ',nums[0])
        a = nums[0]
        print(b)
        print("tortoise",a)
        while a != b:
            a = nums[a]
            print("tortoise",a)
            b = nums[b]
            print("hare",b)
        
        return b

'''
Runtime: 620 ms, faster than 51.88% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 28.1 MB, less than 51.06% of Python3 online submissions for Find the Duplicate Number.
'''
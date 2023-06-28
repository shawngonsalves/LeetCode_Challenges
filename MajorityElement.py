'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        HashMap = {}
        newmax = len(nums)//2
        res, maxCount = 0, 0

        for n in nums:
            HashMap[n] = 1+ HashMap.get(n, 0)
            print(HashMap)
            if HashMap[n] > newmax:
                return n
            res = n if HashMap[n] > maxCount else res
            maxCount = max(HashMap[n], maxCount)
            
        return res



        
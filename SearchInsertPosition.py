'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r = len(nums)-1
        
        
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        
        while l<=r:
            
            m = l+(r-l)//2
            
            if nums[m] >= target:
                
                if nums[m]==target:
                    return m
                else:
                    if nums[m-1] < target:
                        return m
                    else:
                        r=m-1
            else:
                l = m+1

'''
Success
Details 
Runtime: 44 ms, faster than 90.40% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.9 MB, less than 93.13% of Python3 online submissions for Search Insert Position.
'''
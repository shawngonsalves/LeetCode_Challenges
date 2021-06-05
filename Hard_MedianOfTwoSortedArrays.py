'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        print(nums)
        nums.sort()
        n = len(nums)
        if n==1:
            return nums[0]
        if n % 2 != 0:
            return nums[n//2]
        else:
            return (nums[n//2 - 1] + nums[n//2])/2.


'''
Success
Details 
Runtime: 88 ms, faster than 83.14% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 92.55% of Python3 online submissions for Median of Two Sorted Arrays.
'''
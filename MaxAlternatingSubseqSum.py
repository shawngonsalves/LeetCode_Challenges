'''
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 7
Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
Example 2:

Input: nums = [5,6,7,8]
Output: 8
Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
'''

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        evensum,oddsum = 0,0
        
        for i in range(len(nums)-1,-1,-1):
            tempeven = max(oddsum+ nums[i], evensum) 
            tempodd =  max(evensum - nums[i], oddsum)
            
            evensum,oddsum = tempeven,tempodd
        return evensum

'''
Runtime: 1200 ms, faster than 16.67% of Python3 online submissions for Maximum Alternating Subsequence Sum.
Memory Usage: 28.7 MB, less than 33.33% of Python3 online submissions for Maximum Alternating Subsequence Sum.
'''
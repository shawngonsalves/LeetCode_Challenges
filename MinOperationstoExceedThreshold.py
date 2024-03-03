'''
Given nums and integer k.
In one operation we can remove one occurence of smallest element of nums
Return min num of operations so that all elements of the array are greater than or equal to k
'''

class Solution:
    def threshold(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, x in enumerate(nums):
            if x >= k:
                return i
            else:
                return len(nums)
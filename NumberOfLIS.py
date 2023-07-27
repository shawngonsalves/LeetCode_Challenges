# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lenLIS, res = 0, 0
        dp = {} #pair of len,count

        for i in range(len(nums)-1, -1, -1):
            maxLen, maxCount = 1, 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    length, count = dp[j]
                    if length +1 > maxLen:
                        maxLen = length+1
                        maxCount = count

                    elif length +1 == maxLen:
                        maxCount += count

            if  maxLen > lenLIS:
                lenLIS = maxLen
                res = maxCount
            elif maxLen == lenLIS:
                res += maxCount

            dp[i] = [maxLen, maxCount]

        return res

# Runtime 1053 ms Beats 82.56%
# Memory 16.9 MB Beats 19.2%
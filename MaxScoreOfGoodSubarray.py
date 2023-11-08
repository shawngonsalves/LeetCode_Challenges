'''
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
'''

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        cur_min = nums[k]
        res = nums[k]

        while l > 0 or r < len(nums) - 1:
            left = nums[l-1] if l > 0 else 0
            right = nums[r+1] if r < len(nums) -1 else 0
            if left > right:
                l -= 1
                cur_min = min(cur_min, left)
            else:
                r += 1
                cur_min = min(cur_min, right)
            
            res = max(res, cur_min*(r-l+1))

        return res

'''
Runtime 1062 ms Beats 41.21%
Memory 27.3 MB Beats 46.36%
'''
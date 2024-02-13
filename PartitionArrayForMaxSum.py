'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        [1, 15, 7] -> [15,15,15]
        [9,2,5] - > [9,9,9]
        [10] - >[10]
        '''
        cache = {}
        def dfs(i):

            if i in cache:
                return cache[i]

            cur_max = 0
            res = 0

            for j in range(i, min(len(arr), i+k)):
                cur_max = max(cur_max, arr[j])
                window = j - i + 1
                res = max(res, dfs(j+1) + cur_max * window)
            cache[i] = res 
            return res

        return dfs(0)

'''
Runtime 364 ms Beats 34.31% of users with Python3
Memory 17.98 MB Beats 23.83% of users with Python3
'''
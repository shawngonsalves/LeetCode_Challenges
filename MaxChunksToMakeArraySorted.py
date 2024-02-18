'''
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
'''

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        min_val, max_val = min(arr), max(arr)

        if min_val == arr[-1] or max_val ==arr[0]:
            return 1
        max_yet = 0
        chunks = 0
        for ind, val in enumerate(arr): # check for max impact of val
        # 
            
        #     0, 1, 2, 3,  4, 5,   6, 7, 8
        #     $3, 0, 1, 2, $5, 4, $8, 7, 6
        #     ----------->|---->|------->

        # 
            if max_yet < val:
                max_yet = val
            if ind == max_yet:
                chunks += 1
                max_yet = 0

        return chunks
    
'''
Runtime 29 ms Beats 93.00% of users with Python3
Memory 16.54 MB Beats 70.65% of users with Python3
    '''
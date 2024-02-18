'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)        
        heap = list(count.values())
        heapq.heapify(heap)
        res = len(heap)
        
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
                
        return res

'''
Runtime 359 ms Beats 55.66% of users with Python3
Memory 33.39 MB Beats 84.81% of users with Python3
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)     

        freq_list = [0] * (len(arr)+ 1) # freq -:> #of elements w that freq

        for f in count.values():
            freq_list[f] += 1
        res = len(count)

        for f in range(1, len(freq_list)):
            remove = freq_list[f]

            if k >= f * remove:
                k -= f * remove
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        return res

'''
Runtime 316 ms Beats 92.47% of users with Python3
Memory 33.31 MB Beats 84.81% of users with Python3
'''

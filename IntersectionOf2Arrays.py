'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
            
        return res

'''
Runtime 54 ms Beats 29.95% of users with Python3
Memory 16.78 MB Beats 52.43% of users with Python3
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s2 = set(nums2)

        ans = set()
        for x in nums1:
            if x in s2:
                ans.add(x)

        return ans
    
'''
Runtime 36 ms Beats 98.34% of users with Python3
Memory 16.64 MB Beats 91.17% of users with Python3
'''
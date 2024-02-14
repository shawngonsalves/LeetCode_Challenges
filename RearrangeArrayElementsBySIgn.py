'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
 

Constraints:

2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for n in nums:
            if n >= 0:
                positive.append(n)
            else:
                negative.append(n)
        res = []
        
        positive = positive[::-1]
        negative = negative[::-1]
 
        
        for i in range(len(nums)- 1):
            if i == 0:
                res.append(positive[-1])
                positive.pop()
            if i % 2 == 0:
                res.append(negative[-1])
                negative.pop()
            else:
                res.append(positive[-1])
                positive.pop()

        return res

'''
Runtime 1051 ms Beats 33.26% of users with Python3
Memory 51.03 MB Beats 6.29% of users with Python3
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = deque()
        negative = deque()

        for n in nums:
            if n >= 0:
                positive.append(n)
            else:
                negative.append(n)
        res = []

        for i in range(len(nums)- 1):
            if i == 0:
                res.append(positive[0])
                positive.popleft()
            if i % 2 == 0:
                res.append(negative[0])
                negative.popleft()
            else:
                res.append(positive[0])
                positive.popleft()

        return res

'''
Runtime 1047 ms Beats 35.42% of users with Python3
Memory 48.05 MB Beats 35.42% of users with Python3
'''
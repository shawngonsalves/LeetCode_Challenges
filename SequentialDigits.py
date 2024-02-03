'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def gen(last, cur):
            if low <= cur <= high:
                ans.append(cur)

            if last <= 9:
                gen(last + 1, cur * 10 + last)
        
        for i in range(1, 10):

            gen(i, 0)
        return sorted(ans)

'''
Runtime 32 ms Beats 78.59% of users with Python3
Memory 16.40 MB Beats 82.57% of users with Python3
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        queue = deque(range(1, 10))
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9: # 123 -> 1230 + 4
                seq = n* 10 + (ones + 1)
                queue.append(seq)
        return res

'''
Runtime 34 ms Beats 70.64% of users with Python3
Memory 16.59 MB Beats 63.61% of users with Python3
'''
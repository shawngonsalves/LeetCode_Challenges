'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        day = 0
        deposit = 1

        while day < n:


            res += deposit
            deposit += 1
            day += 1
        
            if day % 7 == 0:
                deposit = 1 + day // 7

        return res
    
'''
Runtime 45 ms Beats 25.4%
Memory 16.2 MB Beats 40.24%
'''

class Solution:
    def totalMoney(self, n: int) -> int:

        #Solution 2
        weeks = n // 7
        low = 28
        high = 28 + 7 * (weeks - 1)
        res = (weeks * (low + high)  // 2)


        for i in range(n%7):
          res += i + weeks + 1

        return res
    
'''
Runtime 39 ms Beats 60.62%
Memory 16.3 MB Beats 40.24%
'''
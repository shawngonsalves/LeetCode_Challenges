'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0]* (len(num1)+ len(num2))
        
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += digit
                res[i+j+1] +=(res[i+j]//10)
                res[i+j] = res[i+j] % 10

        print(res)
        res = res[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg+=1
            
        res = map(str, res[beg:])
        return "".join(res)
            
'''
Runtime: 288 ms, faster than 6.85% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 99.98% of Python3 online submissions for Multiply Strings.
'''                
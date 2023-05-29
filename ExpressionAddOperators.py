'''
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        s = num
        n = len(s)
        res = []

        def dfs(i,path,cur_num,prev):
            if i == n:
                if cur_num == target:
                    res.append(path)
                return
            
            for j in range(i,n):
                if j > i and s[i] == '0':
                    break
                num = int(s[i:j+1])

                if i ==0:
                    dfs(j+1, path+str(num),cur_num + num, num)
                else:
                    dfs(j+1, path+"+"+str(num),cur_num + num, num)
                    dfs(j+1, path+"-"+str(num), cur_num - num, -num)
                    dfs(j+1, path+"*"+str(num), cur_num-prev+prev*num, prev*num)
        dfs(0,"", 0,0)
        return res
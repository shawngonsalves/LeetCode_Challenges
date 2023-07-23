# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        HashMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


        def backtrack(i, curString):
            if len(curString) == len(digits):
                res.append(curString)
                return
            
            for c in HashMap[digits[i]]:
                backtrack(i+1, curString + c)
        if digits:
            backtrack(0,"")
        return res
    
# Runtime 47 ms Beats 58.43%
# Memory 16.3 MB Beats 57.59%
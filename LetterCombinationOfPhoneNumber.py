'''
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        final = []
        main1 = []
        letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits =='':
            return []
        elif len(digits) == 1:
            return list(letter[digits])
        elif len(digits) == 2:
            chosen1 = str(letter[digits[0]])
            chosen2 = str(letter[digits[1]])
        elif len(digits) == 3:
            chosen = letter[digits[0]] +','+ letter[digits[1]] +','+ letter[digits[2]]
            chosen1 = str(letter[digits[0]])
            chosen2 = str(letter[digits[1]])
            chosen3 = str(letter[digits[2]])

        elif len(digits) == 4:
            chosen = letter[digits[0]] +','+ letter[digits[1]]+','+ letter[digits[2]] +','+ letter[digits[3]]
            chosen1 = str(letter[digits[0]])
            chosen2 = str(letter[digits[1]])
            chosen3 = str(letter[digits[2]])
            chosen4 = str(letter[digits[3]])

        else:
            print('not applicable')

        if len(digits) == 2:
            for i in range(len(letter[digits[0]])):
                for j in range(len(letter[digits[1]])):
                    main = chosen1[i]+chosen2[j]
                    main1.append(main)

            return main1

        elif len(digits) == 3:
            for i in range(len(letter[digits[0]])):
                for j in range(len(letter[digits[1]])):
                    for k in range(len(letter[digits[2]])):   
                        main = chosen1[i]+chosen2[j]+chosen3[k]
                        main1.append(main)

            return main1

        elif len(digits) == 4:
            for i in range(len(letter[digits[0]])):
                for j in range(len(letter[digits[1]])):
                    for k in range(len(letter[digits[2]])):   
                        for l in range(len(letter[digits[3]])): 
                            main = chosen1[i]+chosen2[j]+chosen3[k]+chosen4[l]
                            main1.append(main)

            return main1


'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {"2":"abc",
                       "3":"def",
                       '4':'ghi',
                       '5':'jkl',
                       '6':'mno',
                       '7':'pqrs',
                       '8':'tuv',
                       '9':'wxyz'}
        res = []
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curStr + c)
            
            
        if digits:
            backtrack(0, '')
     
        return res'''

'''
Runtime: 32 ms, faster than 61.97% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.5 MB, less than 30.79% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
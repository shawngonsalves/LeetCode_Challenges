
def number_is_smiling(n):
    visit = set()

    while n != 1 and n not in visit:
        visit.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    print( n == 1)
    return

number_is_smiling(2)

# Write an algorithm to determine if a number n is SMILING. 

# A SMILING number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits. 
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 

# Those numbers for which this process ends in 1 are SMILING. 
# Return true if n is a SMILING number, and false if not. 

# Example 1: 
# Input: n = 19
# Output: true 
# Explanation: 
# 1^2 + 9^2 = 82 
# 8^2 + 2^2 = 68 
# 6^2 + 8^2 = 100 
# 1^2 + 0^2 + 0^2 = 1 

# Example 2: 
# Input: n = 2 
# Output: false

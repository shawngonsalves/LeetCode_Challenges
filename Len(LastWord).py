class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = 0
        for char in s[::-1]:
            if char != ' ':
                count += 1
            elif char == ' ' and count > 0:
                return count
        return count
    
                

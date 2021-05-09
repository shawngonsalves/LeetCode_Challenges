class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        temp = word
        while 1:
            if temp in sequence:
                count+=1
                temp+=word
            else:
                break
        return count
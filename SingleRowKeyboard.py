import numpy as np
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        curr = 0
        ans = 0
        i = 0
        while i < len(word):
            
            h = keyboard.find(word[i])
            ans+= abs(curr-h)
            curr = h
            print(h)
            i+=1
        print(ans)
        return ans
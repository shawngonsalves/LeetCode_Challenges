class Solution:
    def checkValidString(self, s: str) -> bool:
        lMin,lMax = 0, 0

        for c in s:
            if c == '(':
                 lMin,lMax =  lMin + 1,lMax + 1
            elif c ==')':
                lMin,lMax =  lMin - 1,lMax - 1
            else:
                lMin,lMax =  lMin - 1,lMax+1
            if lMax < 0:
                return False
            if lMin < 0:
                lMin = 0
        return lMin == 0

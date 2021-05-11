class Solution:
    def maximumTime(self, time: str) -> str:
        time1 = time.split(':')
        
        hr = time1[0]
        mm = time1[1]
        hello = []
        best1 = 23 
        best2 = 59
        newhr = hr
        if '?' in hr:
            if '?' in hr[0] and '?' in hr[1]:
                newhr = '2'+'3'
            elif '?' in hr[0]:
                if '0' in hr[1] or '1' in hr[1] or '2' in hr[1] or '3' in hr[1]:
                    newhr = '2'+hr[1]
                else:
                    newhr = '1'+hr[1]
            else:
                if '0' in hr[0] or '1' in hr[0]:
                    newhr = hr[0]+'9'
                else:


                    newhr = hr[0]+'3'

        else:
            print('nahh')
        newmm = mm    
        if '?' in mm:
            if '?' in mm[0] and '?' in mm[1]:
                newmm = '5'+'9'
            elif '?' in mm[0]:
                newmm = '5'+mm[1]
            else:
                newmm = mm[0] +'9'
        print((newhr)+':'+(newmm))
        return str((newhr)+':'+(newmm))
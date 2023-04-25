class Solution:
    def longestPalindrome(self, s: str) -> int:
        out = 0
        c = Counter(s)
        print(c)

        x = 0
        newval = sorted(c.values())
        newval.sort(reverse = True)
        print(newval)
        # if val = 1 then use only one of those
        flag = False
        for val in newval:
            if flag:
                if val % 2 != 0 and val > 1:
                    x += val - 1
                if val % 2 == 0:
                    x += val
            else:
                if val % 2 == 0:
                    x += val


                elif val % 2 != 0 and flag == False:
                    x += val
                    flag = True



            
        return x

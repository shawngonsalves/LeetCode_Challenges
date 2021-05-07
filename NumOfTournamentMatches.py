class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0

        while n >= 2:

            if n%2 != 0:
                total += (n - 1)/2
                print('now total is:', total)
                n = ((n - 1)/2) +1
                print('now next round teams are:', n)
            else:
                total += n/2
                print('now total is:', total)
                n = n/2
                print('now next round teams are:', n)
        return int(total)
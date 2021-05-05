class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
         #15
        rate = numExchange #4
        drank = numBottles
        empty = numBottles
        
        while empty>= rate:

            drank+= (empty//rate)
            empty = (empty%rate) +(empty//rate)

            
        return drank    

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        
        for word in path:
            if word == 'N':
                y += 1
            elif word == 'S':                
                y -= 1
            elif word == 'E':
                x += 1
            else:
                x -= 1
            
            if (x,y) in visited:
                return True            
            visited.add((x, y))
            
            
        return False
        

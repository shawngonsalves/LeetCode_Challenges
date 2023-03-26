class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        visit = set()

        def addRoom(r, c):
            if (r < 0 or c < 0 or r == ROWS or c < 0 or c== COLS or (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1

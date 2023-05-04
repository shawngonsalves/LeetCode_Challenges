class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c =="R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            radTurn = R.popleft()
            dirTurn = D.popleft()

            if radTurn < dirTurn:
                R.append(dirTurn + len(senate))
            else:
                D.append(radTurn + len(senate))
            

        return "Radiant" if R else "Dire"

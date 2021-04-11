class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for item in text:
            if item in ('b','a','l','l','o','o','n'):
                d[item] += 1
        if len(d) < 5 or d['l'] == 1 or d['o'] == 1:
            return 0
        
        print(d)
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2
        return min(d.values())

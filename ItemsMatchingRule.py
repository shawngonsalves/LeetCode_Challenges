class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for i,j in enumerate (items):
            if ruleKey == 'type':
                if ruleValue == j[0]:
                    ans+=1
            elif ruleKey == 'color':
                if ruleValue == j[1]:
                    print(j[1])
                    ans +=1
            else:
                if ruleValue == j[2]:
                    ans+=1
        return ans
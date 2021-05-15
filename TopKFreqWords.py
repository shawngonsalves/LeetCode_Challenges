class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if len(words)==0:
            return None
        d= {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        print(d)
        nd = sorted(d.items(),key=lambda num:(-num[1],num[0]))
        ans = []
        for i in range(k):
            ans.append(nd[i][0])
        return ans
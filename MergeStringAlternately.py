class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ''
        s = 0
        while s != len(word1) and s!= len(word2):

            final+= word1[s]

            final+= word2[s]
            s+=1
        if s==len(word1) and s < len(word2):

            final+= word2[s:]
        if s==len(word2) and s< len(word1):

            final+= word1[s:]

        return final
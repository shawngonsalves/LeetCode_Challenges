'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key = lambda x: len(x), reverse = True)
        word_index = {}

        for i, w in enumerate(words):
            word_index[w] = i

        dp = {} # index of word  -> len(longest chain)

        def dfs(i):
            res = 1
            if i in dp:
                return dp[i]
            for j in range(len(words[i])):
                w = words[i]
                pred = w[:j] + w[j+1:]
                if pred in word_index:
                    res = max(res, 1 + dfs(word_index[pred]))
            dp[i] = res
            return res
        
        for i in range(len(words)):
            dfs(i)
        return max(dp.values())
    
'''
Runtime 128 ms Beats 65.1%
Memory 19.3 MB Beats 17.10%
'''